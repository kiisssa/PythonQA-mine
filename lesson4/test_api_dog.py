import pytest
import requests
import json
import unittest.mock
from http import HTTPStatus
import builtins

class TestBreedList():
    base_url = 'https://dog.ceo/api'

    def test_get_status(self):
        response = requests.get(self.base_url + '/breeds/image/random')
        print (response.status_code)
        assert response.status_code == HTTPStatus.OK

    @unittest.mock.patch('builtins.input', lambda: 'russell')
    def test_is_breed_exist(self):
        response = requests.get(self.base_url + '/breeds/list/all')
        assert response.status_code == 200
       # print (json.loads(response.content))
        breeds = json.loads(response.content)['message']
        assert input() in breeds['terrier']

    @pytest.mark.parametrize('breed, sub_breed', [('terrier','russell'), ('schipperke',[])])
    def test_breed_and_sub_exist(self, breed, sub_breed):
        response = requests.get(self.base_url + '/breeds/list/all')
        assert response.status_code == HTTPStatus.OK
        breeds = json.loads(response.content)['message']
        assert breed in breeds
        print(breeds[breed])
        if breeds[breed]:
            assert sub_breed in breeds[breed]
        else:
            assert (not sub_breed and not breeds[breed])



    @pytest.mark.parametrize('breed, sub_breed', [('hound', 'afghan')])
    def test_random(self, breed, sub_breed):
        response = requests.get(self.base_url + '/breed/hound/list')
        assert response.status_code == HTTPStatus.OK
        sub_breeds = json.loads(response.content)['message']
        assert sub_breed in sub_breeds
        print (sub_breeds)


    @pytest.mark.parametrize('route, quantity', [
        ('hound/afghan', 3),
        ('hound/afghan', 5)
    ])
    def test_image_quantity(self, route, quantity):
        response = requests.get(self.base_url + '/breed/' + route + '/images/random/' + str(quantity))
        assert response.status_code == HTTPStatus.OK
        images = json.loads(response.content)['message']
        print (type (images))
        print (len(images))
        assert len(images) == quantity

