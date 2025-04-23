import pytest
import httpx


NOT = "Not Offensive"
NOT_LIST = [
    "I like you",
    "You are fine",
    "Great weather",
    "I don't like you",
    "I might fall in love with u"
]

OFF = "Offensive"
OFF_LIST = [
    "I hate you",
    "You are very stupid",
    "Shut up!",
    "What an idiot..."
]


def test_ping_server():
    assert httpx.get('http://localhost:8000/ping').status_code == 200


@pytest.mark.parametrize("text", NOT_LIST)
def test_not_offensive(text):
    response = httpx.get(f'http://localhost:8000/analyze-text/{text}')
    result = response.json()['results']['result']
    assert result == NOT


@pytest.mark.parametrize("text", OFF_LIST)
def test_offensive(text):
    response = httpx.get(f'http://localhost:8000/analyze-text/{text}')
    result = response.json()['results']['result']
    assert result == OFF
