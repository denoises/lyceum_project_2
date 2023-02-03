import pygame
import os
import sys
import random

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
clock = pygame.time.Clock()
rand_gen_for_clouds = int(random.randint(0, 10))



# нужно прибавлять переменную self.ind_light если игрок начинает проигрывать НА ДАННЫЙ МОМЕНТ НЕ ГОТОВО
class Light(pygame.sprite.Sprite):
    def __init__(self):
        super(Light, self).__init__()
        self.ind_light = 0
        self.img_light = [
            pygame.image.load('other/light/0.png').convert_alpha(),
            pygame.image.load('other/light/10.png').convert_alpha(),
            pygame.image.load('other/light/20.png').convert_alpha(),
            pygame.image.load('other/light/30.png').convert_alpha(),
            pygame.image.load('other/light/40.png').convert_alpha(),
            pygame.image.load('other/light/50.png').convert_alpha(),
            pygame.image.load('other/light/80.png').convert_alpha(),
            pygame.image.load('other/light/100.png').convert_alpha()
        ]

    def light_raise(self):
        print('light_raise')
        if self.ind_light < 8:
            self.ind_light += 1
            screen.blit(self.img_light[self.ind_light])

    def light_lower(self):
        print('light_lower')
        if self.ind_light > 0:
            self.ind_light -= 1
            screen.blit(self.img_light[self.ind_light])


class Clouds:  # задумка хорошая, но реализовать нормально сложно
    def __init__(self):
        self.clouds_img = [pygame.image.load('other/clouds/1.png'),
                           pygame.image.load('other/clouds/2.png'),
                           pygame.image.load('other/clouds/3.png'),
                           pygame.image.load('other/clouds/4.png'),
                           pygame.image.load('other/clouds/5.png'),
                           pygame.image.load('other/clouds/6.png'),
                           pygame.image.load('other/clouds/7.png'),
                           pygame.image.load('other/clouds/8.png'),
                           pygame.image.load('other/clouds/9.png'),
                           pygame.image.load('other/clouds/10.png')
                           ]

    def render(self):
        img_clouds = self.clouds_img[rand_gen_for_clouds]
        img_clouds = pygame.transform.scale(img_clouds, (1920, 1080))
        screen.blit(img_clouds, (0, 0))
