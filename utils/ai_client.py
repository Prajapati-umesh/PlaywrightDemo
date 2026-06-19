from typing import Any


class AiClient:
    def __init__(self, endpoint: str, api_key: str):
        self.endpoint = endpoint.rstrip("/")
        self.api_key = api_key

    def request(self, payload: dict[str, Any]) -> dict[str, Any]:
        # Placeholder for AI service integration
        return {
            "endpoint": self.endpoint,
            "payload": payload,
            "status": "mocked",
        }
