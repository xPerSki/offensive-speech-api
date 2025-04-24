# Offensive Speech API

---
## Usage
### Building Docker Image
```bash
docker build -t offensive-speech-api .
```
### Running the Container
```bash
docker run -p 8000:8000 offensive-speech-api
```

## Endpoints

### `/ping`
Health check, returns "pong"

### `/analyze-text/<text>`
Analyzes the provided text for offensive content.
Replace `<text>` with the text you want to analyze.

## Example Response:
```json
{
    "results": {
        "text": "Example text",
        "result": "Not Offensive",
        "confidence": "95.3"
    }
}
```

## Running local server
```bash
uvicorn app.server-app:app --host 0.0.0.0 --port 8000
```
```python
python app/server-app.py
```

## Running Tests
**Make sure that your server is running**
```bash
pytest tests
```
