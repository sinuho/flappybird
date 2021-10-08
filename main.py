
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
flying = False
game_over = False

#load images
bg_img = pygame.image.load('resources/bg.png', 'backgound')
ground_img = pygame.image.load('resources/ground.png', 'ground')

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f"resources/bird{num}.png")
            self.images.append(img)
            print("sth")
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self):

        if flying is True:
            #gravity
            self.vel += 0.5
            if self.vel > 12:
                self.vel = 12
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)
        #jump
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            self.vel = -10
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #handle the animation
        self.counter += 1
        flap_cooldown = 5

        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0

        self.image = self.images[self.index]

        #rotate the bird
        self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)

bird_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))

bird_group.add(flappy)



run = True
while run:

    clock.tick(fps)

    #draw background
    screen.blit(bg_img, (0,0))

    bird_group.draw(screen)
    bird_group.update()



    #check if bird has hit the ground
    if flappy.rect.bottom > 767:
        game_over = True
        flying = False


    #draw ground
    screen.blit(ground_img, (ground_scroll, 769))
    if game_over == False:
        ground_scroll -= scroll_speed

        if abs(ground_scroll) > 35:
            ground_scroll = 0

    #QUIT THE GAME
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True

    pygame.display.update()

pygame.quit()