from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

#def client(mocker):
#    # Mocking the FastAPI app instance
#    return TestClient(mocker.patch("main.app", autospec=True))

def test_status_code():
    response = client.get("/")
    assert response.status_code == 200

def test_response():
    response = client.get("/")
    assert response.json() == {"greeting":"Hello world this is the new file"}
