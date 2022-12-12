import pytest
from src.model.Graph import *
from src.model.BFS import *


def pytest_namespace():
    return {'bfs': 0, 'start': 0, 'end': 0}


@pytest.fixture()
def resourse_setup(request):
    Graph(300, 300, 100)
    pytest.bfs = BFS()
    pytest.start = 1
    pytest.end = 5


@pytest.fixture()
def resourse_setup_min(request):
    Graph(300, 300, 3)
    pytest.bfs = BFS()
    pytest.start = 1
    pytest.end = 2


@pytest.fixture()
def resourse_setup_max(request):
    Graph(300000, 300000, 1000000)
    pytest.bfs = BFS()
    pytest.start = 100
    pytest.end = 502000


def test_translate_wrong_input(resourse_setup):
    with pytest.raises(ValueError):
        pytest.bfs.translate('pdpkfnrjef')


def test_bfs(resourse_setup):
    pytest.bfs.bfs(pytest.start, pytest.end)


def test_bfs_min(resourse_setup_min):
    pytest.bfs.bfs(pytest.start, pytest.end)


def test_bfs_big(resourse_setup_max):
    pytest.bfs.bfs(pytest.start, pytest.end)


def test_bfs_wrong_input(resourse_setup):
    with pytest.raises(ValueError):
        pytest.bfs.bfs('pdpkfnrjef', 'ghfh')
