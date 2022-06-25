import pytest


@pytest.fixture()
def tes1():
    a = 'leo'
    print('\n传出a')
    return a


@pytest.fixture(scope='function')
def tes2():
    b = '男'
    print('\n传出b')
    return b


class TestCase:
    @pytest.mark.usefixtures('tes1')
    def test_3(self):
        name = 'leo'
        print('找到name')
        assert tes1 == name

    def test_4(self, tes2):
        sex = '男'
        print('找到sex')
        assert tes2 == sex














