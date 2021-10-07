
import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

#define game variables
ground_scroll = 0
scroll_speed = 3
num = 1

#load images
bg_img = pygame.image.load('resources/bg.png', 'backgound')
ground_img = pygame.image.load('resources/ground.png', 'ground')

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'resources/bird{num}.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

bird_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))

bird_group.add(flappy)



run = True
while run:

    clock.tick(fps)

    #draw background
    screen.blit(bg_img, (0,0))

    bird_group.draw(screen)

    #draw ground
    screen.blit(ground_img, (ground_scroll, 769))
    ground_scroll -= scroll_speed

    if abs(ground_scroll) > 35:
        ground_scroll = 0

    #QUIT THE GAME
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    pygame.display.update()

pygame.quit()