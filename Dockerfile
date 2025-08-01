FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    espeak ffmpeg libespeak1 libportaudio2 \
    && apt-get clean

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
