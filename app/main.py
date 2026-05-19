from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

LMSTUDIO_URL = os.getenv("LMSTUDIO_URL", "http://localhost:1234/v1/chat/completions")

app = FastAPI(title="Local LLM API", version="1.0")

class ChatRequest(BaseModel):
    prompt: str
    max_tokens: int = 2048
    temperature: float = 0.3

@app.post("/chat")
def chat(request: ChatRequest):
    payload = {
        "model": "deepseek-r1-0528-qwen3-8b",
        "messages": [{"role": "user", "content": request.prompt}],
        "max_tokens": request.max_tokens,
        "temperature": request.temperature
    }

    response = requests.post(LMSTUDIO_URL, json=payload)
    response.raise_for_status()

    data = response.json()
    msg = data["choices"][0]["message"]

    final_answer = ""

    # Case 1: DeepSeek returns content as a list of chunks
    if isinstance(msg.get("content"), list):
        for chunk in msg["content"]:
            if isinstance(chunk, dict) and "text" in chunk:
                final_answer += chunk["text"]

    # Case 2: content is a normal string
    elif isinstance(msg.get("content"), str):
        final_answer = msg["content"]

    # Case 3: fallback to reasoning_content (rare)
    if not final_answer:
        final_answer = msg.get("reasoning_content", "")

    return {"response": final_answer}
