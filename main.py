import pygame
import consts
import Screen

state={"window_open":True,"is_winning":0,"show":False,"move":None,"soldier_place":(0,0),
       }
def main():
    pygame.init()

    while True:
        Screen.draw_game()

if __name__ == "__main__":
    main()