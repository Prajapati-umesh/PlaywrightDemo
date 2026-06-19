from utils.ai_client import AiClient


def test_ai_client_request():
    client = AiClient(endpoint="https://ai.example.com", api_key="fake-key")
    response = client.request({"prompt": "Test prompt"})

    assert response["status"] == "mocked"
    assert response["endpoint"] == "https://ai.example.com"
