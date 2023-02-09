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

    def render_10(self):
        self.image_light = pygame.transform.scale(self.img_light[1], (1920, 1080))
        screen.blit(self.image_light, (0, 0))
    def render_20(self):
        self.image_light = pygame.transform.scale(self.img_light[2], (1920, 1080))
        screen.blit(self.image_light, (0, 0))
    def render_30(self):
        self.image_light = pygame.transform.scale(self.img_light[3], (1920, 1080))
        screen.blit(self.image_light, (0, 0))
    def render_40(self):
        self.image_light = pygame.transform.scale(self.img_light[4], (1920, 1080))
        screen.blit(self.image_light, (0, 0))
    def render_50(self):
        self.image_light = pygame.transform.scale(self.img_light[5], (1920, 1080))
        screen.blit(self.image_light, (0, 0))
    def render_80(self):
        self.image_light = pygame.transform.scale(self.img_light[6], (1920, 1080))
        screen.blit(self.image_light, (0, 0))
    def render_100(self):
        self.image_light = pygame.transform.scale(self.img_light[7], (1920, 1080))
        screen.blit(self.image_light, (0, 0))



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
