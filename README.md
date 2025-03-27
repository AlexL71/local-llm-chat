# Local LLM Assistant

A private, offline AI assistant that lives on your phone — powered by a local model running on your PC.  
No cloud, no data leaks, no limits. Just your own setup, fully under your control.

---

## What I Built

-  A **mobile chat app** using Flutter
-  A **FastAPI server** to handle chat requests
-  A local **DeepSeek 7B LLM** running with Ollama
-  Connected everything over **local Wi-Fi / hotspot**

---

##  How It Works

1. Phone app sends your message over local Wi-Fi
2. FastAPI server on your PC receives the message
3. Server forwards it to DeepSeek via Ollama
4. DeepSeek generates a reply and sends it back to your phone

---
## How to Run It

###  On the PC (Server + LLM)

```bash
# 1. Start DeepSeek in Ollama
ollama run deepseek-llm:7b

# 2. Start the FastAPI server
cd llm_server
uvicorn server:app --host 0.0.0.0 --port 8000

```bash
# On the Phone
Connect your phone to your PCs hotspot or same Wi-Fi

Open the Flutter app (already installed)

Start chatting with DeepSeek fully offline!