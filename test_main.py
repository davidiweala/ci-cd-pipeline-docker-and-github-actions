import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

from main import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['Status'] == 'Success'

def test_david():
    client = app.test_client()
    response = client.get('/david')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Healthy'