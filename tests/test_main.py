
import pytest
from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)

#def client(mocker):
#    # Mocking the FastAPI app instance
#    return TestClient(mocker.patch("main.app", autospec=True))
@pytest.fixture
def mock_database_url(monkeypatch):
    monkeypatch.setenv('DATABASE_URL', 'test_database_url')
    assert os.environ.get('DATABASE_URL') == 'test_database_url'

def test_status_code():
    response = client.get("/")
    assert response.status_code == 200

def test_response():
    response = client.get("/")
    assert response.json() == "NOVI - Comic books API"

def test_response_schema_500():
    response = client.get("/comics/schema-check")
    assert response.status_code == 500
