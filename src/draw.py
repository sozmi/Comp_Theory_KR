from model.Vertex import *
from model.Edge import *
from model.Graph import *
from random import randint
from model.BFS import *
from model.DFS import *
import pygame

__isDraw = False


def close_plt():
    setDraw(False)
    print("close")


def setDraw(value):
    __isDraw = value


def getDraw():
    return __isDraw

def drawDFS(start, search, n):
    if (getDraw()):
        return
    setDraw(True)
    pygame.init()
    SIZE = WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Графы")
    g = Graph.random(300, 300, n)
    dfs = DFS()
    name = chr(A_ASCII + search % 33) * ((33 + search) // 33)
    name2 = chr(A_ASCII + start % 33) * ((33 + start) // 33)

    dfs.translate(g)

    dfs.dfs(start, search)
    font = pygame.font.Font(None, 25)
    textEnd = ''

    text1 = font.render("Ищем " + name + " из вершины " + name2, True,
                        (0, 0, 0))
    text2 = font.render(name + " найдена", True, (0, 0, 0))

    textRect1 = pygame.Rect(10, 10, 100, 30)
    textRect2 = pygame.Rect(500, 10, 100, 30)

    tB_end = pygame.Rect(10, 570, 600, 30)
    for elem in dfs.endList:
        name = (chr(A_ASCII + elem % 33) * ((33 + elem) // 33))
        textEnd = textEnd + ' ' + name
    textEnd = font.render(textEnd, True, (0, 0, 0))
    selectBox = 0
    running = True
    while running:

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

        screen.fill((255, 255, 255))

        g.update()
        g.draw(screen)

        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        screen.blit(textEnd, tB_end)

        pygame.display.flip()

    pygame.quit()
def drawBFS(start, search, n):
    if (getDraw()):
        return
    setDraw(True)
    pygame.init()
    SIZE = WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Графы")
    g = Graph.random(300, 300, n)
    bfs = BFS()
    name = chr(A_ASCII + search % 33) * ((33 + search) // 33)
    name2 = chr(A_ASCII + start % 33) * ((33 + start) // 33)

    bfs.translate(g)

    bfs.bfs(start, search)
    font = pygame.font.Font(None, 25)
    textEnd = ''

    text1 = font.render("Ищем " + name + " из вершины " + name2, True,
                        (0, 0, 0))
    text2 = font.render(name + " найдена", True, (0, 0, 0))

    textRect1 = pygame.Rect(10, 10, 100, 30)
    textRect2 = pygame.Rect(500, 10, 100, 30)

    tB_end = pygame.Rect(10, 570, 600, 30)
    for elem in bfs.endList:
        name = (chr(A_ASCII + elem % 33) * ((33 + elem) // 33))
        textEnd = textEnd + ' ' + name
    textEnd = font.render(textEnd, True, (0, 0, 0))
    selectBox = 0
    running = True
    while running:

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

        screen.fill((255, 255, 255))

        g.update()
        g.draw(screen)

        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        screen.blit(textEnd, tB_end)

        pygame.display.flip()

    pygame.quit()
