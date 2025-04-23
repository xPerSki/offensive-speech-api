import pytest
import sys
import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))
import nlp_analyzer as analyzer


NOT = "Not Offensive"
OFF = "Offensive"

NOT_LIST = [
    "I like you",
    "Hope to see you soon!",
    "Wish you luck",
    "I don't like you",
    "You are not my friend",
    "Get off my lawn!",
    "Be quiet now, kid",
    "Pass me the salt, buddy"
]

OFF_LIST = [
    "I hate you",
    "You are stupid",
    "Shut up!",
    "You're an idiot"
]


@pytest.fixture(scope="module")
def model_and_tokenizer():
    model_name = "cardiffnlp/twitter-roberta-base-offensive"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return model, tokenizer


@pytest.mark.parametrize("text", NOT_LIST)
def test_not_offensive(model_and_tokenizer, text):
    model, tokenizer = model_and_tokenizer
    assert analyzer.analyze_text(text, model, tokenizer) == NOT


@pytest.mark.parametrize("text", OFF_LIST)
def test_offensive(model_and_tokenizer, text):
    model, tokenizer = model_and_tokenizer
    assert analyzer.analyze_text(text, model, tokenizer) == OFF
