from flask import Flask, request, Response, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

OLLAMA_BASE_URL = "http://localhost:11434"

@app.route("/api/chat", methods=["POST"])
def chat():
    # Parse JSON while request context is active
    payload = request.get_json()
    # Streaming generator
    def generate():
        with requests.post(f"{OLLAMA_BASE_URL}/api/chat", json=payload, stream=True) as r:
            r.raise_for_status()
            for chunk in r.iter_content(chunk_size=None):
                if chunk:
                    yield chunk
    return Response(generate(), content_type="application/json")

@app.route("/api/pull", methods=["POST"])
def pull_model():
    # Parse JSON while request context is active
    payload = request.get_json()
    # Streaming generator for model download
    def generate():
        with requests.post(f"{OLLAMA_BASE_URL}/api/pull", json=payload, stream=True) as r:
            r.raise_for_status()
            for chunk in r.iter_content(chunk_size=None):
                if chunk:
                    yield chunk
    return Response(generate(), content_type="application/json")

@app.route("/api/tags", methods=["GET"])
def list_models():
    # Get list of available models
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags")
        response.raise_for_status()
        return Response(response.content, content_type="application/json")
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/generate", methods=["POST"])
def generate_single():
    # For single non-chat generations (used for model testing)
    payload = request.get_json()
    def generate():
        with requests.post(f"{OLLAMA_BASE_URL}/api/generate", json=payload, stream=True) as r:
            r.raise_for_status()
            for chunk in r.iter_content(chunk_size=None):
                if chunk:
                    yield chunk
    return Response(generate(), content_type="application/json")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
