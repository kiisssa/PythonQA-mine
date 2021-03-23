import requests

def test_answer(base_url, status_code):
    response = requests.get(base_url)
    assert response.status_code == int(status_code)


