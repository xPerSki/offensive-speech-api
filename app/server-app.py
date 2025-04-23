from fastapi import FastAPI
import uvicorn
from app import nlp_analyzer

app = FastAPI()


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
            "result": result
        }
    }


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host='0.0.0.0')
