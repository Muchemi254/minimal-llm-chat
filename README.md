# Minimal LLM Chat UI + Proxy for Ollama

A lightweight, zero-install (static HTML) chat UI for Ollama, with a tiny Flask proxy backend for CORS support.  
Designed as a minimal, resource-friendly alternative to OpenWebUI.

## ✨ Features
- 📜 Chat with memory & session management
- 🖥️ Works entirely in the browser (frontend is a single HTML file)
- ⚡ Ultra-lightweight Flask proxy (no database, no heavy server)
- 🔄 Model loading, listing, and pulling directly from the UI
- 💾 Save, import, and export chats (stored in browser localStorage)
- 📱 Mobile-friendly responsive layout

## 📂 Project Structure
minimal-llm-chat/
├── backend/
│   └── ollama_proxy.py
├── frontend/
│   └── minimal_llm_chat.html
├── requirements.txt
