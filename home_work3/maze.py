'''
сундук - экипировка ~ +5 здоровье
монстр - битва
ключ -  единственный
портал - открыть дверь ключом ~ выход
ловушка - сжирает характеристики
'''

import random
inventory = []
health = int(200)
size_maze = int(10)
i = int(0)
j = int(0)
rooms = ["пусто", "сундук", "монстр", "ловушка"]
# единственные - "ключ", "портал"
rows, cols = size_maze, size_maze
maze = [[[] for j in range(rows)] for i in range(cols)]
for i in range(rows):
    for j in range(cols):
        if i == 0 and j == 0:
            maze[i][j].append("пусто")
        else:
            maze[i][j].append(rooms[random.randint(0, 3)])

def move(my_move: str, i: int, j:int) -> list:
    if my_move == "вправо":
        if (i == 0):
            print("Там стена - передумайте")
            new_move = input()
            move(new_move)
        else:
            if maze[i][j] == "пусто":
                empty()
            elif maze[i][j] == "сундук":
                chest()
            elif maze[i][j] == "монстр":
                monster()
            elif maze[i][j] == "ловушка":
                trap()
            elif maze[i][j] == "ключ":
                key()
            elif maze[i][j] == "портал":
                portal()
    elif my_move == "влево":
    elif my_move == "вверх":
    elif my_move == "вниз":

def empty():

def chest():

def monster():

def key():

def portal():

def trap():
