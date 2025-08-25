import random

import consts
from consts import *
mine_palces=[]

def create ():
    possible_place=[]
    for i in range(consts.BOARD_LENGHT):
        for j in range (consts.BOARD_WIDTH):
            my_tuple=(j+1,i+1)
            possible_place.append(my_tuple)


    board_matrix= []
    for i in range(consts.BOARD_LENGHT):
        board_matrix.append([])
        for j in range (consts.BOARD_WIDTH):
            board_matrix[i].append(['free'])


    for i in range (consts.MINE_NUM):
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

    return mine_palces






