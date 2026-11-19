from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from app_rag_assistant.config import Settings, get_settings
from app_rag_assistant.main import create_app


@pytest.fixture
def client() -> Iterator[TestClient]:
    app = create_app()
    app.dependency_overrides[get_settings] = lambda: Settings(environment="test")
    with TestClient(app) as test_client:
        yield test_client


def test_health_returns_ok(client: TestClient) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "environment": "test"}
