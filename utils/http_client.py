import requests
from typing import Any


class HttpClient:
    def __init__(self, base_url: str, headers: dict[str, str] | None = None):
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {"Content-Type": "application/json"}

    def _url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def get(self, path: str, params: dict[str, Any] | None = None, **kwargs) -> requests.Response:
        return requests.get(self._url(path), headers=self.headers, params=params, **kwargs)

    def post(self, path: str, json: Any | None = None, **kwargs) -> requests.Response:
        return requests.post(self._url(path), headers=self.headers, json=json, **kwargs)

    def put(self, path: str, json: Any | None = None, **kwargs) -> requests.Response:
        return requests.put(self._url(path), headers=self.headers, json=json, **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        return requests.delete(self._url(path), headers=self.headers, **kwargs)
