import pytest
from src.model.Graph import *
from src.model.DFS import *
def pytest_namespace():
    return {'dfs': 0, 'start': 0, 'end': 0}


@pytest.fixture()
def resourse_setup(request):
    Graph(300, 300, 100)
    pytest.dfs = DFS()
    pytest.start = 1
    pytest.end = 5


@pytest.fixture()
def resourse_setup_min(request):
    Graph(300, 300, 3)
    pytest.dfs = DFS()
    pytest.start = 1
    pytest.end = 2


@pytest.fixture()
def resourse_setup_max(request):
    Graph(300000, 300000, 1000000)
    pytest.dfs = DFS()
    pytest.start = 100
    pytest.end = 502000


def test_translate_wrong_input(resourse_setup):
    with pytest.raises(ValueError):
        pytest.bfs.translate('pdpkfnrjef')


def test_dfs(resourse_setup):
    pytest.dfs.dfs(pytest.start, pytest.end)


def test_dfs_min(resourse_setup_min):
    pytest.dfs.dfs(pytest.start, pytest.end)


def test_dfs_big(resourse_setup_max):
    pytest.dfs.dfs(pytest.start, pytest.end)


def test_dfs_wrong_input(resourse_setup):
    with pytest.raises(ValueError):
        pytest.dfs.dfs('pdpkfnrjef', 'ghfh')
