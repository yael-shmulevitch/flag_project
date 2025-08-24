import pygame


screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def draw(place):
    img = pygame.image.load(bubble["color"])
    screen.blit(img,(bubble["center_x"],bubble["center_y"]))