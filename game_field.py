import random
from consts import *
mine_palces=[]

def create ():
    possible_place=[]
    for i in range(25):
        for j in range (50):
            my_tuple=(j+1,i+1)
            possible_place.append(my_tuple)


    board_matrix= []
    for i in range(25):
        board_matrix.append([])
        for j in range (50):
            board_matrix[i].append(['free'])


    for i in range (20):
        row= random.randint(0,BOARD_LENGHT-1)
        col= random.randint(0,BOARD_WIDTH-4)
        if board_matrix[row][col]==['free'] and board_matrix[row][col+1]==['free'] and board_matrix[row][col+2]==['free']:
            board_matrix[row][col] = MINE
            mine_palces.append((col, row))
            board_matrix[row][col+1] = MINE
            mine_palces.append((col, row+1))
            board_matrix[row][col+2] = MINE
            mine_palces.append((col, row+2))

        else:
            continue

    for i in range (len(board_matrix)):
        print (board_matrix[i])

    return mine_palces



