import pytest

class TestList:

    @pytest.fixture()
    def fruits_list(self):
        return ['apple', 'orange', 'banana', 'pineapple', 'lemon']

    def test_fruits_list_1(self, fruits_list):
      assert isinstance(fruits_list, list)

    def test_fruits_list_2(self, fruits_list):
      assert fruits_list == ['apple', 'orange', 'banana', 'pineapple', 'lemon']
      print("list is correct")

    def test_fruits_list_3(self, fruits_list):
      print('lemon=', fruits_list.count('lemon'))
      print('fruits=', len(fruits_list))
      assert len(fruits_list) == 5

    def test_fruits_list_4(self, fruits_list):
      fruits_list.append('cucumber')
      assert 'cucumber' in fruits_list
      print(fruits_list)

    def test_fruits_list_5(self, fruits_list):
      fruits_list.reverse()
      assert fruits_list == ['lemon', 'pineapple', 'banana', 'orange', 'apple']
      print(fruits_list)