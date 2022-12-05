import math
import sys
sys.path.insert(1, 'D:\\University\\3_course\\Теория алгоритмов\\Курсач\\src\\model')
from random import randint, random
import Vertex
from Edge import *
from GraphObject import GraphObject

A_ASCII = 65  # A ascii letter constant

class Graph(GraphObject):
    def __init__(self, matrix, verticies, edges):
        self.matrix = matrix
        self.verticies = verticies
        self.edges = edges
        self.objects = self.edges + self.verticies
 
    def __len__(self):
        return len(self.verticies)
 
    def draw(self, surface):
        [obj.draw(surface) for obj in self.objects]
 
    def update(self):
        [obj.update() for obj in self.objects]
 
    def get_event(self, ev):
        [obj.get_event(ev) for obj in self.objects]
 
    def set_width(self, width):
        if not(isinstance(width, int)):
            raise ValueError('Ширина должна быть числом!')
        [setattr(obj, "width", width) for obj in self.objects]
 
    @classmethod
    def random(cls, x, y, n, weights=(1, 10), radius=250, fill_factor=0.3, vsize=15, width=1, color=(0, 0, 0)):  # randomly generated Graph        
        matrix = [[0]*n for _ in range(n)]
        verticies = []
        edges = []
 
        angle = 2 * math.pi / n
        for i in range(n):
            name = chr(A_ASCII + i % 33) * ((33 + i) // 33)
            vx, vy = radius*math.cos(angle*i)+x, radius*math.sin(angle*i)+y
            verticies.append(Vertex(name, int(vx), int(vy), vsize, color, width))
 
        for i in range(n-1):
            for j in range(i+1, n):
                if random() > fill_factor:
                    continue
                weight = randint(*weights)
                matrix[i][j] = matrix[j][i] = weight
                edges.append(Edge(verticies[i], verticies[j], weight, color, width))
 
        return cls(matrix, verticies, edges)