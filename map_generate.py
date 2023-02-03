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

scores = 1000  # баллы

rand_gen_for_patern = [random.randint(0, 9) for i in range(162)]
rand_gen_for_clouds = int(random.randint(0, 10))


class Tree_class:  # это что, елка?
    def __init__(self, min_x_tree, max_x_tree, min_y_tree, max_y_tree):
        self.min_x_tree = min_x_tree
        self.max_x_tree = max_x_tree
        self.min_y_tree = min_y_tree
        self.max_y_tree = max_y_tree

    def tree(self, screen):
        # большой и разнообразный выбор
        tree_image = [pygame.image.load('image/low_settings/tree/el0001.png').convert_alpha(),
                      pygame.image.load('image/low_settings/tree/el0002.png').convert_alpha(),
                      pygame.image.load('image/low_settings/tree/el0003.png').convert_alpha(),
                      pygame.image.load('image/low_settings/tree/el0004.png').convert_alpha(),
                      pygame.image.load('image/low_settings/tree/el0005.png').convert_alpha(),
                      pygame.image.load('image/low_settings/tree/el0006.png').convert_alpha(),
                      pygame.image.load('image/low_settings/tree/el0007.png').convert_alpha(),
                      pygame.image.load('image/low_settings/tree/el0008.png').convert_alpha(),
                      pygame.image.load('image/low_settings/tree/el0009.png').convert_alpha(),
                      pygame.image.load('image/low_settings/tree/el0010.png').convert_alpha(),
                      ]

        # max_y_tree = 0
        # min_y_tree = 1080
        # max_x_tree = 1920
        # min_x_tree = 0
        cal_tree_max = 200  # количество елок
        cal_tree_now = 0

        while cal_tree_now < cal_tree_max:
            tree_image_random = tree_image[random.randint(0, 9)]
            a = random.randint(300, 430)
            tree_image_random_scale = pygame.transform.scale(tree_image_random, (a, a))  # рандомный размер елок

            proverka = 0
            while proverka == 0:
                random_y_cooord = random.randint(-300, 1080)
                random_x_cooord = random.randint(-300, 1920)
                if 500 < random_x_cooord < 1100 and 150 < random_y_cooord < 650:  # область для костра
                    proverka = 0
                else:
                    proverka = 1

            screen.blit(tree_image_random_scale,
                        (random_x_cooord, random_y_cooord))  # отрисовка ёлок
            cal_tree_now += 1


class Board:  # доска?
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        # картинки из которых делается выбор
        sp_ground = (pygame.image.load('image/low_settings/new_ground/ground0000.png').convert_alpha(),
                     pygame.image.load('image/low_settings/new_ground/ground0001.png').convert_alpha(),
                     pygame.image.load('image/low_settings/new_ground/ground0002.png').convert_alpha(),
                     pygame.image.load('image/low_settings/new_ground/ground0003.png').convert_alpha(),
                     pygame.image.load('image/low_settings/new_ground/ground0004.png').convert_alpha(),
                     pygame.image.load('image/low_settings/new_ground/ground0005.png').convert_alpha(),
                     pygame.image.load('image/low_settings/new_ground/ground0006.png').convert_alpha(),
                     pygame.image.load('image/low_settings/new_ground/ground0007.png').convert_alpha(),
                     pygame.image.load('image/low_settings/new_ground/ground0008.png').convert_alpha(),
                     pygame.image.load('image/low_settings/new_ground/ground0009.png').convert_alpha(),
                     )
        for y in range(self.height):
            for x in range(self.width):
                # случайно выбираем картинку
                img_ground = sp_ground[rand_gen_for_patern[y * 18 + x]]
                # подгоняем размеры
                self.small_img_ground = pygame.transform.scale(img_ground, (155, 155))
                # выстраиваем из них сетку
                screen.blit(self.small_img_ground, (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                                    self.cell_size, self.cell_size))
