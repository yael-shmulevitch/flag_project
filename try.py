import pygame
import consts
import time
screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.init()


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


