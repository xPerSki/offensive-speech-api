from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL_NAME = "cardiffnlp/twitter-roberta-base-offensive"
MODEL = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
TOKENIZER = AutoTokenizer.from_pretrained(MODEL_NAME)


def cleanup_text(text) -> str:
    clean_text = text
    for char in text:
        if not char.isalpha() and char != ' ':
            clean_text = clean_text.replace(char, '')
    return clean_text


def analyze_text(text, model, tokenizer, verbose=False) -> dict:
    text = cleanup_text(text)
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)

    labels = ["Not Offensive", "Offensive"]
    predicted_label = labels[torch.argmax(probs)]
    confidence = f"{max(probs[0]*100):.1f}"
    print(f"Predicted label: {predicted_label} [{confidence}%]") if verbose else None
    return {"predicted_label": predicted_label, "confidence": confidence}


if __name__ == "__main__":
    import pc_utils
    import asyncio

    async def main():
        text = input("Text: ")
        print("Loading model...")
        asyncio.create_task(pc_utils.cpu_watcher(60, False))
        await asyncio.sleep(0)

        analyze_text(text, MODEL, TOKENIZER, verbose=True)

    asyncio.run(main())
