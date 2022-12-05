import pytest
import sys
sys.path.insert(1, 'D:\\University\\3_course\\Теория алгоритмов\\Курсач\\src\\model')
from Graph import *
from BFS import *

def test_translate_wrong_input():
    g = Graph(300,300,100)
    bfs = BFS()
    with pytest.raises(ValueError): 
        bfs.translate('pdpkfnrjef')

def test_bfs():
    g = Graph(300,300,100)
    bfs = BFS()
    bfs.bfs(1,5)

def test_bfs_min():
    g = Graph(300,300,3)
    bfs = BFS()
    bfs.bfs(1,2)

def test_bfs_big():
    g = Graph(300000,300000,1000000)
    bfs = BFS()
    bfs.bfs(10,502531)

def test_bfs_wrong_input():
    g = Graph(300,300,100)
    bfs = BFS()
    with pytest.raises(ValueError): 
        bfs.bfs('pdpkfnrjef', 'ghfh')