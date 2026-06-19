from utils.http_client import HttpClient


class SampleApi:
    def __init__(self, base_url: str):
        self.client = HttpClient(base_url)

    def get_health(self):
        return self.client.get("/health")
