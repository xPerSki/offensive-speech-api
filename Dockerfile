FROM python:3.10-slim

WORKDIR /app-api

COPY app ./app
COPY tests ./tests
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt  \
    && pip install --no-cache-dir pytest

CMD ["python", "app/main.py"]
