from utils.http_client import HttpClient


def test_api_health_endpoint(config):
    api_client = HttpClient(config.get_env("api_base_url"))
    response = api_client.get("/health")

    assert response.status_code == 200
    assert response.json().get("status") == "ok"
