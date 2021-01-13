import pytest

class TestString:
    @pytest.fixture()
    def str(self):
        return 'newtest'

    @pytest.fixture()
    def line(self):
        return 'simpleline'

    def test_string_1(self, str):
        str = str * 2
        assert str == 'newtestnewtest'
        print(str)

    def test_string_2(self,str):
        assert str.split('t') == ['new', 'es', '']
        print(str.split('t'))

    def test_string_3(self, str):
        assert len(str) == 7
        print(len(str))

    def test_string_4(self, str, line):
        str = (str + line) * 2
        assert str.swapcase() == 'NEWTESTSIMPLELINENEWTESTSIMPLELINE'
        print(str.swapcase())

    def test_string_5(self, line):
        assert line[:6] == 'simple'
        print(line[:6])
