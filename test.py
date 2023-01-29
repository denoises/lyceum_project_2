import pygame
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('AxeMan')
clock = pygame.time.Clock()
direction = True
image = [pygame.image.load(r'image/low_settings/person/right/right0001.png'),
         pygame.image.load(r'image/low_settings/person/left/left0001.png')]
x = 100
y = 100
person_speed = 20
run = True
while run:
    clock.tick(60)
    window.fill((255, 255, 255))
    if direction == True:
        window.blit(image[0], (x, y))
    if direction == False:
        window.blit(image[1], (x, y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = True
            elif event.key == pygame.K_LEFT:
                direction = False
    key_pressed_is = pygame.key.get_pressed()
    if key_pressed_is[K_LEFT] and x >= -40:
        x -= person_speed
    if key_pressed_is[K_RIGHT] and x <= 1700:
        x += person_speed
    if key_pressed_is[K_UP] and y > -100:
        y -= person_speed
    if key_pressed_is[K_DOWN] and y < 970:
        y += person_speed
    pygame.display.update()
