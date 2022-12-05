import pytest
import sys
sys.path.insert(1, 'D:\\University\\3_course\\Теория алгоритмов\\Курсач\\src\\model')
from Graph import *
from DFS import *


def test_translate_wrong_input():
    g = Graph(300,300,100)
    dfs = DFS()
    with pytest.raises(ValueError): 
        dfs.translate('pdpkfnrjef')

def test_dfs():
    g = Graph(300,300,100)
    dfs = DFS()
    dfs.dfs(1,5)

def test_dfs_min():
    g = Graph(300,300,3)
    dfs = DFS()
    dfs.dfs(1,2)

def test_dfs_big():
    g = Graph(300000,300000,1000000)
    dfs = DFS()
    dfs.dfs(10,502531)

def test_dfs_wrong_input():
    g = Graph(300,300,100)
    dfs = DFS()
    with pytest.raises(ValueError): 
        dfs.dfs('pdpkfnrjef', 'ghfh')