import random
import pygame
import consts
import game_field


screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def draw_flag():
    img_flag = pygame.image.load(consts.FLAG)
    screen.blit(img_flag,(47*20,22*20))


def grass():
    possible_place=[]
    for i in range(25):
        for j in range (50):
            my_tuple=(j+1,i+1)
            possible_place.append(my_tuple)
    grass_place=[]
    for i in range(20):
        x=random.choice(possible_place)
        grass_place.append(x)
        possible_place.remove(x)
    return grass_place

MY_GRASS_PLACE=grass()

def draw_grass():
    img = pygame.image.load(consts.GRASS)
    for i in range (len(MY_GRASS_PLACE)):
        screen.blit(img,(MY_GRASS_PLACE[i][0]*20,MY_GRASS_PLACE[i][1]*20))






def draw_soldier(soldier_place):
    img = pygame.image.load(consts.SOLDIER)
    screen.blit(img,(soldier_place[0]*20,soldier_place[1]*20))



def draw_mine(mine_places):
    img = pygame.image.load(consts.MINE)
    for i in range(len(mine_places)):
        if i%3==0:
            screen.blit(img, (mine_places[i][0]*20,mine_places[i][1]*20))

def draw_grid():
    screen.fill(consts.BG_MATRIX)
    for x in range(0, consts.WINDOW_WIDTH, consts.BLOCK_SIDE):
        for y in range(0, consts.WINDOW_HEIGHT, consts.BLOCK_SIDE):
            rect = pygame.Rect(x, y, consts.BLOCK_SIDE, consts.BLOCK_SIDE)
            pygame.draw.rect(screen, consts.GRID_COLOR, rect, 1)
    draw_soldier(soldier_place=(0,0))
    draw_mine([(0,4),(100,200)])
    pygame.display.flip()
    while 1:
        pass


def draw_message(message, font_size, color, bg, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color,bg)
    screen.blit(text_img, location)

def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.FONT_SIZE,
                 consts.MESSAGE_COLOR, consts.MESSAGE_BG_WIN, consts.LOCATION)

def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.FONT_SIZE,
                 consts.MESSAGE_COLOR,consts.MESSAGE_BG_LOSE, consts.LOCATION)

def draw_game(state,mine_places):
    if state["show"]==True:
        draw_grid()
    else:
        screen.fill(consts.BG_COLOR)
        draw_flag()
        draw_grass()
        draw_soldier(state["soldier_place"])
        draw_mine(mine_places)
        pygame.display.flip()

