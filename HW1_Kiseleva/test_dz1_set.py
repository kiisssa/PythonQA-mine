import pytest

class TestSet:

    @pytest.fixture()
    def set_new(self):
        return {0, 1, 1, 2, 3, 5, 8, 13, 21}

    @pytest.fixture()
    def set_other(self):
        return {0, 1, 2, 3}

    def test_set_new_1(self, set_new):
        assert isinstance(set_new, set)
        print(set_new)

    def test_set_new_2(self, set_new):
        assert len(set_new) == 8
        print(len(set_new))

    def test_set_new_3(self, set_new):
        set_new.add(22)
        assert set_new == {0, 1, 2, 3, 5, 8, 13, 21, 22}
        print(set_new)

    def test_set_new_4(self, set_new, set_other):
       set_new.intersection(set_other)
       assert set_new.intersection(set_other) == {0, 1, 2, 3}
       print (set_new.intersection(set_other))

    def test_set_new_5(self, set_new, set_other):
        set_other.issubset(set_new)
        assert set_other.issubset(set_new) == True
        print (set_other.issubset(set_new))
