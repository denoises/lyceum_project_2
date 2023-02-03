import pygame
import os
import sys
import random
from load_image import load_image

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()


# Стартовое окно
def start_screen():
    intro_text = ("Ваша цель - выжить в этом лесу",
                  '(Нажмите любую кнопку чтобы начать игру)', ""
                  )

    fon = pygame.transform.scale(load_image('image/axeman.png'), (1920, 1080))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()


def cursor():  # курсор
    image_cursor = load_image('image/navigate.png')
    image_cur = pygame.transform.scale(image_cursor, (25, 25))
    cursor = pygame.sprite.Sprite()
    cursor.image = image_cur
    cursor.rect = cursor.image.get_rect()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(cursor)
    pygame.mouse.set_visible(False)
