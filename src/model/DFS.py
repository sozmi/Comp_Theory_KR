import pygame
from .Vertex import *
from .Edge import *
from .Graph import *
from .AlgObject import AlgObject
from random import randint
from collections import defaultdict


class DFS(AlgObject):
    adjList = defaultdict(list)
    endList = []

    def __init__(self):
        return

    def translate(self, gr):
        'Обработчик ошибок'
        if not (isinstance(gr, Graph)):
            raise ValueError('В функцию должен быть подан граф')
        for i in range(len(gr.matrix)):
            for j in range(len(gr.matrix[i])):
                if gr.matrix[i][j] > 0:
                    self.adjList[i].append(j)

    visited = set()  # Set to keep track of visited nodes of graph.
    skip = False

    def dfs(self, node, end):  #function for dfs
        if self.skip == True:
            return
        'Обработчик ошибок'
        if not (isinstance(node, int)):
            raise ValueError('Начальный элемент должен быть числом')
        if not (isinstance(end, int)):
            raise ValueError('Искомый элемент должен быть числом')
        if node not in self.visited:
            self.endList.append(node)
            if node == end:
                print(chr(A_ASCII + node % 33) * ((33 + node) // 33))
                self.skip = True
                return
            print(chr(A_ASCII + node % 33) * ((33 + node) // 33))
            self.visited.add(node)
            for neighbour in self.adjList[node]:
                self.dfs(neighbour, end)

    '''def dfs(self, node, elem):
        'Обработчик ошибок'
        if not(isinstance(node, int)):
            raise ValueError('Начальный элемент должен быть числом')
        if not(isinstance(elem, int)):
            raise ValueError('Искомый элемент должен быть числом')
        if node not in self.visited:
            self.endList.append(node)
            print(chr(A_ASCII + node % 33) * ((33 + node) // 33))
            if elem == node:
                return
            self.visited.add(node)
            for neighbour in self.adjList[node]:
                print('Enter me')
                self.dfs(neighbour, elem)'''