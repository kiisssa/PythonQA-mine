import pytest
import random
import requests
import json
import unittest.mock
from http import HTTPStatus

class TestPlaceholderList():
    base_url = 'https://jsonplaceholder.typicode.com/'

    def test_get_status(self):
        response = requests.get(self.base_url + 'guide')
        print (response.status_code)
        assert response.status_code == HTTPStatus.OK

    @pytest.mark.parametrize('id', [1, 2, 3])
    @unittest.mock.patch('builtins.input', lambda: 'omnis laborum odio')
    def test_album(self, id):
        response = requests.get(self.base_url + 'albums/' + str(id))
        assert response.status_code == HTTPStatus.OK
        albums = json.loads(response.content)
        print (albums)
        assert input() in albums['title']

    @pytest.mark.parametrize('postId', [1, 2, 3, 4, 5])
    def test_post_comment(self, postId):
        response = requests.get(self.base_url + 'posts/' + str(postId) + '/comments')
        assert response.status_code == HTTPStatus.OK
        posts = json.loads(response.content)
        assert len(posts) == 5

    @pytest.mark.parametrize('input_id, output_id', [('101', '101')])
    @pytest.mark.parametrize('input_title, output_title', [('title', 'title')])
    def test_api_post_request(self, input_id, output_id, input_title, output_title):
        response = requests.post(
        self.base_url + 'posts',
        data={'title': input_title, 'body': 'bar', 'userId': input_id})
        response_json = response.json()
        assert response_json['title'] == output_title
        assert response_json['body'] == 'bar'
        assert response_json['userId'] == output_id
        print (response_json)

    @pytest.mark.parametrize('input_id, output_id', [('100', '100')])
    @pytest.mark.parametrize('input_title, output_title', [('title', 'title')])
    def test_api_delete_request(self, input_id, output_id, input_title, output_title):
        response = requests.post(
        self.base_url + 'posts' + input_id,
        data={'title': input_title, 'body': 'bar', 'userId': input_id})
        response_json = response.json()
        assert response_json == {}
        print (response_json)