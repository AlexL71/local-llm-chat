import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow your phone to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatInput(BaseModel):
    message: str

@app.post("/chat")
async def chat(input: ChatInput):
    user_msg = input.message

    # Talk to Ollama (DeepSeek 7B)
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "deepseek-llm:7b",
            "prompt": user_msg,
            "stream": False
        }
    )

    if response.status_code == 200:
        data = response.json()
        return {"response": data["response"]}
    else:
        return {"response": "❌ Error from Ollama."}
