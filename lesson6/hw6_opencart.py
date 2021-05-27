from http import HTTPStatus
import requests

def test_first(browser, base_url):
    browser.get(base_url)
    response = requests.get(base_url)
    assert response.status_code == HTTPStatus.OK
