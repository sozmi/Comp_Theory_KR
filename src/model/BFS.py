import pygame
from .Vertex import *
from .Edge import *
from .Graph import *
from .AlgObject import AlgObject
from random import randint
from collections import defaultdict


class BFS(AlgObject):
    adjList = defaultdict(list)

    def __init__(self):
        return

    def translate(self, gr):
        'Обработчик ошибок'
        if not(isinstance(gr, Graph)):
            raise ValueError('В функцию должен быть подан граф')
        for i in range(len(gr.matrix)):
            for j in range(len(gr.matrix[i])):
                if gr.matrix[i][j] > 0:
                    self.adjList[i].append(j)
        print("The list")
        for elem in self.adjList:
            print(str(elem))

    visited = [] # List for visited nodes.
    queue = []     #Initialize a queue
    endList = []

    def bfs(self, node, element): #function for BFS
        'Обработчик ошибок'
        if not(isinstance(node, int)):
            raise ValueError('Начальный элемент должен быть числом')
        if not(isinstance(element, int)):
            raise ValueError('Искомый элемент должен быть числом')
        self.visited.append(node)
        self.queue.append(node)
        while self.queue:          # Creating loop to visit each node
            m = self.queue.pop(0)
            print(chr(A_ASCII + m % 33) * ((33 + m) // 33)) 
            self.endList.append(m)
            if element == m:
                return
                    
            for neighbour in self.adjList[m]:
                if neighbour not in self.visited:
                    self.visited.append(neighbour)
                    self.queue.append(neighbour)