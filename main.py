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
        Soldier.keyboard(state)
        state["is_winning"]=Soldier.check(state["soldier_place"],mine_places)
        Screen.draw_game(state,mine_places)
        if state["is_winning"]==0:
            pass
        elif state["is_winning"]==1:
            print("winner")
        elif state["is_winning"] == 2:
            print("loser")

if __name__ == "__main__":
    main()