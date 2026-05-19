# **README.md**

# 🚀 Local LLM API (FastAPI + LM Studio)

A lightweight, container‑friendly API layer that exposes a **local Large Language Model** (DeepSeek‑R1, Qwen, Llama, etc.) running inside **LM Studio** through a clean, OpenAI‑style `/chat` endpoint.

This project lets you:

- Run an LLM **fully offline**
- Interact with it through a simple REST API
- Containerize the API using Docker
- Swap models in LM Studio without changing your code

Perfect for local development, automation, and private AI workflows.

---

## ✨ Features

- **FastAPI** backend with a `/chat` endpoint  
- **OpenAI‑compatible request format**  
- Works with **LM Studio’s local server**  
- Supports DeepSeek‑R1 reasoning + final answer extraction  
- Docker‑ready  
- Easy to extend with more endpoints  

---

## 📦 Requirements

- **LM Studio** (running on your machine)
- **Python 3.10+**
- **Docker** (optional but recommended)

---

## 🧠 LM Studio Setup

1. Open LM Studio  
2. Load your model (e.g., `deepseek-r1-0528-qwen3-8b`)  
3. Go to **Local Server**  
4. Enable:

   - **Start Server**
   - **Serve on Local Network** (important for WSL/Docker)

5. Note the server URL, usually:

```
http://localhost:1234/v1/chat/completions
```

If you’re using WSL or Docker, you may need to use your Windows host IP instead.

---

## ⚙️ Environment Variable

The API reads the LM Studio URL from:

```
LMSTUDIO_URL
```

Default (if not set):

```
http://localhost:1234/v1/chat/completions
```

You can override it:

```bash
export LMSTUDIO_URL=http://<your-ip>:1234/v1/chat/completions
```

---

## ▶️ Running Locally (without Docker)

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 🐳 Running with Docker

Build the image:

```bash
docker build -t llm-api .
```

Run the container:

```bash
docker run -p 8000:8000 llm-api
```

If using WSL, add host mapping:

```bash
docker run \
  --add-host=host.docker.internal:host-gateway \
  -p 8000:8000 \
  llm-api
```

---

## 📡 API Usage

### **POST /chat**

Request:

```json
{
  "prompt": "Explain how transformers work",
  "max_tokens": 2048,
  "temperature": 0.3
}
```

Response:

```json
{
  "response": "Transformers work by using self-attention..."
}
```

---

## 🗂 Project Structure

```
LLM-experiment/
│
├── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🧩 How It Works

- FastAPI receives your prompt  
- It forwards the request to LM Studio  
- LM Studio runs the model locally  
- The API extracts the **final answer** (not chain‑of‑thought)  
- Returns clean JSON  

---

## 🛠 Customization

You can easily modify:

- Default model  
- System prompts  
- Token limits  
- Additional endpoints  
- Logging / debugging  

---

## 🤝 Contributing

Feel free to open issues or submit pull requests.

---

## 📄 License

MIT License
