import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

def test_home_data(client):
    response = client.get('/')
    assert response.data == b'Hello, Docker CI/CD!'

def test_page_not_found(client):
    response = client.get('/this_page_does_not_exist')
    assert response.status_code == 404

def test_home_post_method_not_allowed(client):
    response = client.post('/')
    assert response.status_code == 405

def test_home_content_type(client):
    response = client.get('/')
    assert response.headers['Content-Type'] == 'text/html; charset=utf-8'
