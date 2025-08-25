import pygame
import consts
import Screen
from Screen import draw_win_message, draw_lose_message
from game_field import *
import Soldier

state={"window_open":True,"is_winning":0,"show":False,"move":None,"soldier_place":(0,0),
       }
def main():
    pygame.init()
    mine_places = create()
    my_grass= Screen.grass()
    while state["window_open"]:
        state["soldier_place"]=Soldier.keyboard(state)
        Soldier.check(state["soldier_place"],mine_places)
        if state["is_winning"]==1:
            pass
        elif state["is_winning"]==2:
            pass
        else:
            pass
        Screen.draw_game(state,mine_places)



if __name__ == "__main__":
    main()