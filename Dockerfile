FROM python:3.10-slim

WORKDIR /app-api

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir pytest

COPY app ./app
COPY tests ./tests
RUN cp app/nlp_analyzer.py tests/

CMD ["uvicorn", "app.server-app:app", "--host", "0.0.0.0", "--port", "8000"]
