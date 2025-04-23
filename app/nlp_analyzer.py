from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL_NAME = "cardiffnlp/twitter-roberta-base-offensive"
MODEL = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
TOKENIZER = AutoTokenizer.from_pretrained(MODEL_NAME)


def analyze_text(text, model, tokenizer, verbose=False) -> str:
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)

    labels = ["Not Offensive", "Offensive"]
    predicted_label = labels[torch.argmax(probs)]
    print(f"Predicted label: {predicted_label} [{max(probs[0])*100:.1f}%]") if verbose else None
    return predicted_label


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
