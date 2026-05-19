FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

ENV LMSTUDIO_URL=http://172.29.80.1:1234/v1/chat/completions

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
