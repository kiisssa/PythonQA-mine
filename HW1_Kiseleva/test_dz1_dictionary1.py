import pytest

class TestDictionary:

    @pytest.fixture()
    def dictionary(self):
        return {'street1': 'Sadovaya', 'street2': 'Zelenina', 'street3': 'Rokossovskogo', 'street4': 'Yralskaya'}

    def testIsDictionary(self, dictionary):
        assert isinstance(dictionary, dict)

    def testIsStreet1HasRightName(self, dictionary):
        assert dictionary['street1'] == 'Sadovaya'

    def testIsDictHasAllKeysAndValues(self, dictionary):
        assert list(dictionary) == ['street1', 'street2', 'street3', 'street4']
        assert list(dictionary.values()) == ['Sadovaya', 'Zelenina', 'Rokossovskogo', 'Yralskaya']

    def test_dct_3(self, dictionary):
        del dictionary['street2']
        assert list(dictionary.values()) == ['Sadovaya', 'Rokossovskogo', 'Yralskaya']

    def testIsCopyDictSame(self, dictionary):
        newDictionary = dictionary.copy()
        assert newDictionary == dictionary
