
from difflib import restore


def test_hello_world_returns_page(client):
    response = client.get('/')
    assert response.status_code == 200
