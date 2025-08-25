import pygame
import consts
import Screen
from Screen import draw_win_message, draw_lose_message
from game_field import *
import Soldier
from time import sleep
import time

state={"window_open":True,"is_winning":0,"show":False,"move":None,"soldier_place":(0,0),
       }
def main():
    pygame.init()
    mine_places = create()
    while state["window_open"]:
        Soldier.keyboard(state)
        if state["show"]==True:
            ending=time.time()+1
            while time.time()<ending:
                Screen.draw_game(state,mine_places)
            state["show"]=False
        else:
            state["is_winning"]=Soldier.check(state["soldier_place"],mine_places)
            Screen.draw_game(state, mine_places)


if __name__ == "__main__":
    main()