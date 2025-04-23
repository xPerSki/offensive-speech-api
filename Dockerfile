FROM python:3.10-slim

WORKDIR /app-api

COPY app ./app
COPY tests ./tests
COPY requirements.txt .

RUN cp app/nlp_analyzer.py tests/

RUN pip install --no-cache-dir -r requirements.txt  \
    && pip install --no-cache-dir pytest

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
