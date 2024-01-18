
import pytest
import os
import requests

#def client(mocker):
#    # Mocking the FastAPI app instance
#    return TestClient(mocker.patch("main.app", autospec=True))
@pytest.fixture
def mock_database_url(monkeypatch):
    monkeypatch.setenv('DATABASE_URL', 'test_database_url')
    assert os.environ.get('DATABASE_URL') == 'test_database_url'

def test_status_code():
    response = requests.get("http://api:8000")
    assert response.status_code == 200

def test_response():
    response = requests.get("http://127.0.0.1:8000")
    assert response.json() == "NOVI - Comic books API"
