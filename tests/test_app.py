import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    rv = client.get('/')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['message'] == "Hello from Docker CI/CD Pipeline! 🚀"
    assert 'timestamp' in json_data

def test_health(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    assert rv.get_json()['status'] == 'healthy'

def test_users(client):
    rv = client.get('/api/users')
    assert rv.status_code == 200
    users = rv.get_json()
    assert len(users) == 2
    assert users[0]['name'] == 'Amol Kharat'