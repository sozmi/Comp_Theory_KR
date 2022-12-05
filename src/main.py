import tkinter as tk
from tkinter import *
import draw

n = 9


def check2(param):
    try:
        i_pr = int(param) >= 0
        if (i_pr >= 0 and i_pr < n):
            return True
    except ValueError:
        print("That's not an int!")
        return False


def check():
    fr = from_index.get()
    to = to_index.get()
    if (check2(fr) and check2(to)):
        return [int(fr), int(to)]
    return 0


def startBFS():
    res = check()
    if (res != 0):
        draw.drawBFS(res[0], res[1], n)


def startDFS():
    res = check()
    if (res != 0):
        draw.drawDFS(res[0], res[1], n)


def addGraphParam():
    global n
    try:
        param = count.get()
        i_pr = int(param)
        if (i_pr >= 10 and i_pr <= 100):
            n = i_pr
            newWindow.destroy()
    except ValueError:
        print("That's not an int!")


def cancel():
    newWindow.destroy()


def startCreate():
    global newWindow, count
    photo_ok = PhotoImage(file="src\\res\\btn_ok.png").subsample(3, 3)
    photo_cancel = PhotoImage(file="src\\res\\btn_cancel.png").subsample(3, 3)
    newWindow = tk.Toplevel(root, padx=20, pady=20)
    Label(newWindow, text='Количество вершин',
          font=('Verdana', 13)).pack(side=TOP, pady=10)
    count = Entry(newWindow, font=('Verdana', 13))
    count.pack()

    Button(newWindow,
           command=addGraphParam,
           width=70,
           height=30,
           image=photo_ok).pack(side='left', anchor='e', expand=True)
    Button(newWindow, command=cancel, width=80, height=30,
           image=photo_cancel).pack(side='right', anchor='w', expand=True)
    newWindow.mainloop()


def exit_main():
    global root
    root.destroy()


root = Tk()
global from_index, to_index
photo_bfs = PhotoImage(file="src\\res\\btn_bfs.png").subsample(3, 3)
photo_dfs = PhotoImage(file="src\\res\\btn_dfs.png").subsample(3, 3)
photo_create = PhotoImage(file="src\\res\\btn_create.png").subsample(3, 3)
photo_exit = PhotoImage(file="src\\res\\btn_exit.png").subsample(3, 3)

Label(root, text='BFS&DFS', font=('Verdana', 15)).pack(side=TOP, pady=10)
Label(root, text='Из вершины:', font=('Verdana', 15)).pack()
from_index = Entry(root, font=('Verdana', 13))
from_index.pack()
Label(root, text='В вершину:', font=('Verdana', 15)).pack()
to_index = Entry(root, font=('Verdana', 13))
to_index.pack()

Button(root, command=startBFS, width=200, height=60, image=photo_bfs).pack()

Button(root, command=startDFS, width=200, height=60, image=photo_dfs).pack()
Button(root, command=startCreate, width=200, height=60,
       image=photo_create).pack()
Button(root, command=quit, width=200, height=60, image=photo_exit).pack()
root.protocol("WM_DELETE_WINDOW", exit_main)
root.mainloop()
