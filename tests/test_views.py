
from difflib import restore


def test_hello_world_returns_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'</form>' in response.data


def test_upload_file_prints_error(client):
    response = client.post('/upload/')
    assert response.status_code == 302
    assert response.headers.get('Location') == '/?error=1'

