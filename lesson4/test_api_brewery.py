import pytest
import requests
import json
import unittest.mock
from http import HTTPStatus
#from jsonschema import validate

class TestBreweryList():
    base_url = 'https://api.openbrewerydb.org/breweries/'

    def test_get_status(self):
        response = requests.get(self.base_url + '/search?query=dog')
        print (response.status_code)
        assert response.status_code == HTTPStatus.OK

    def test_records_quantity(self):
        response = requests.get(self.base_url + '?by_state=ohio')
        print(response.status_code)
        assert response.status_code == HTTPStatus.OK
        ohio = list(json.loads(response.content))
        print(len(ohio))
        assert len (ohio) == 20

    @unittest.mock.patch('builtins.input', lambda: 'Cincinnati')
    def test_getting_exact_record(self):
        response = requests.get(self.base_url + '5494')
        assert response.status_code == 200
        user = json.loads(response.content)
        print(user.items())
        assert user['id'] == 5494
        assert input() in user['city']

    @pytest.mark.parametrize('route, quantity', [
        ('dog', 10),
        ('dog', 20)
    ])
    def test_brewery_quantity(self, route, quantity):
        response = requests.get(self.base_url + '/search?query=' + route)
        print(response.status_code)
        assert response.status_code == HTTPStatus.OK
        dog = json.loads(response.content)
        print(len(dog))
        print(dog[quantity])
        assert dog[10] == {'id': 5359, 'name': 'Boss Dog Brewing', 'brewery_type': 'brewpub', 'street': '2179 Lee Rd',
                           'address_2': None, 'address_3': None, 'city': 'Cleveland', 'state': 'Ohio',
                           'county_province': None, 'postal_code': '44118-2907', 'country': 'United States',
                           'longitude': '-81.5652955454545', 'latitude': '41.5003064545455', 'phone': '2163212337',
                           'website_url': 'http://www.bossdogbrewing.com', 'updated_at': '2018-08-24T15:43:28.002Z',
                           'created_at': '2018-07-24T01:33:59.648Z'}
        assert dog[20] == {'id': 1902, 'name': 'Dog Rose Brewing Company', 'brewery_type': 'micro',
                           'street': '77 Bridge St', 'address_2': None, 'address_3': None, 'city': 'Saint Augustine',
                           'state': 'Florida', 'county_province': None, 'postal_code': '32084-4335',
                           'country': 'United States', 'longitude': '-81.3130666785714', 'latitude': '29.8894814642857',
                           'phone': '9042173355', 'website_url': 'http://www.dogrosebrewing.com',
                           'updated_at': '2018-08-24T00:27:09.144Z', 'created_at': '2018-07-24T01:33:12.641Z'}

    @pytest.mark.parametrize('route, quantity', [
            ('dog', [3]),
            ('cat', [5])
        ])
    def test_brewery_quantity(self, route, quantity):
            response = requests.get(self.base_url + '/autocomplete?query=' + route + str(quantity))
            print(response.status_code)
            assert response.status_code == HTTPStatus.OK
            query = json.loads(response.content)
            print(query)
            assert len(query) == 15



    @pytest.mark.parametrize('id, name', [('2268', 'Laughing Dog Brewing')])
    #@pytest.mark.parametrize('id, name', [('3068', 'Sea Dog Brewing')])
    def test_random(self, id, name):
        response = requests.get(self.base_url + 'autocomplete?query=dog')
        assert response.status_code == HTTPStatus.OK
        searches = json.loads(response.content)
        print (searches)
        #assert len(searches) == 15
        #print (type(searches))
        assert searches[3] == {'id' : id, 'name' : name}
       # assert searches[5] == {'id' : id, 'name' : name}






