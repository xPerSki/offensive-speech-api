from fastapi import FastAPI
import uvicorn
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from app import nlp_analyzer

app = FastAPI()


@app.get("/")
def default():
    return "Offensive Speech API - Connected"


@app.get("/ping")
def ping():
    return "pong"


@app.get("/analyze-text/{text}")
def analyze_text(text: str):
    model = nlp_analyzer.MODEL
    tokenizer = nlp_analyzer.TOKENIZER
    result = nlp_analyzer.analyze_text(text, model, tokenizer)
    return {
        "results": {
            "text": text,
            "result": result["predicted_label"],
            "confidence": result["confidence"]
        }
    }


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host='localhost')
