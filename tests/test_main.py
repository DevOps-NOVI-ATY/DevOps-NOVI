import pytest
from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)

@pytest.fixture
def mock_database_url(monkeypatch):
    monkeypatch.setenv('DATABASE_URL', 'test_database_url')
    assert os.environ.get('DATABASE_URL') == 'test_database_url'

# Use the TestClient with the fixture
def test_status_code(mock_database_url):
    
    response = client.get("/")
    assert response.status_code == 200

# Use the TestClient with the fixture
def test_response(mock_database_url):
    response = client.get("/")
    assert response.json() == {"greeting": "Hello world this is the new file"}