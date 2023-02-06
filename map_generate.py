import pygame
import os
import sys
import random
from person import Person

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
clock = pygame.time.Clock()

scores = 1000  # баллы

rand_gen_for_patern = [random.randint(0, 9) for i in range(162)]
player = Person()
x_pers_g = player.x
y_pers_g = player.y


class Tree_class:  # это что, елка?
    def __init__(self, min_x_tree, max_x_tree, min_y_tree, max_y_tree):
        global x_pers_g, y_pers_g

        self.min_x_tree = min_x_tree
        self.max_x_tree = max_x_tree
        self.min_y_tree = min_y_tree
        self.max_y_tree = max_y_tree

        self.speed_pers = player.speed_pers
        self.x_pers = player.x
        self.y_pers = player.y
        print(self.x_pers, self.y_pers)

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

        self.cal_tree_max = 50  # количество елок
        self.cal_tree_now = 0
        self.tree_image_random_scale = []
        self.random_x_cooord = []
        self.random_y_cooord = []
        generation_of_trees = []

        self.num_el = 0
        while self.cal_tree_now < self.cal_tree_max:
            tree_image_random = tree_image[random.randint(0, 9)]
            a = random.randint(300, 430)
            self.tree_image_random_scale.append(
                pygame.transform.scale(tree_image_random, (a, a)))  # рандомный размер елок

            proverka = 0
            while proverka == 0:
                random_x_cooord_1 = random.randint(-300, 1920)
                random_y_cooord_1 = random.randint(-300, 1080)

                if 500 < random_x_cooord_1 < 1100 and 150 < random_y_cooord_1 < 650:  # область для костра
                    proverka = 0
                else:
                    proverka = 1
                    self.random_x_cooord.append(random_x_cooord_1)
                    self.random_y_cooord.append(random_y_cooord_1)
                self.num_el += 1

            self.cal_tree_now += 1

    def render_tree(self):
        n = 0
        while n < self.cal_tree_max:
            # надо как то понять как получать координаты персонажа в даеный момент
            print(self.x_pers, self.y_pers)  # вот эти координаты
            pers_rect = pygame.image.load(
                # это коллизая персонажа, первый параметр - картинка, как я понял она просто для понимания высоты и шиниры, второй и третий координаты
                f"image/low_settings/person_take-throw/down/person_take-throw_down0001.png").get_rect(
                topleft=(self.x_pers, self.y_pers))
            el_rect = self.tree_image_random_scale[n].get_rect(  # тоже самое с ёлкой
                topleft=(self.random_x_cooord[n], self.random_y_cooord[n]))

            if el_rect.colliderect(pers_rect):  # коллизия елки пересеккает персонажа то
                self.tree_image_random_scale.pop(n)  # вычеркиваем всё о этой ёлке из списка
                self.random_x_cooord.pop(n)
                self.random_y_cooord.pop(n)
                self.cal_tree_max -= 1
            else:  # иначе рисуем
                screen.blit(self.tree_image_random_scale[n],
                            (self.random_x_cooord[n], self.random_y_cooord[n]))  # отрисовка ёлок
            n += 1  # по идеи мы просто в предыдущий иф должны засунут проверку нажатия клавиши и всё. Но проблемма с понимаение как сделать коллизию у этих картинок


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


def main():
    global which_way, scores, x_pers_g, y_pers_g
    which_way = 'down'
    speed_pers = 3

    screen = pygame.display.set_mode(size)
    number_while = 0
    number_event = 0
    number_clikov = 0

    board = Board(18, 9)
    # clouds = Clouds()

    board.set_view(0, 0, 150)
    treeeeee = Tree_class(0, 1920, 1080, 0)

    treeeeee.tree(screen)

    running = True
    pygame.init()

    run_gr = True
    while run_gr:
        treeeeee.tree(screen)
        run_gr = False
    while running:
        number_while += 1
        for event in pygame.event.get():
            number_event += 1
            if event.type == pygame.QUIT:
                running = False

            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_UP):
                y_pers_g -= speed_pers
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_DOWN):
                y_pers_g += speed_pers
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_LEFT):
                x_pers_g -= speed_pers
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_RIGHT):
                x_pers_g += speed_pers

            # что то на подобии ускорения, нужно допиливать
            if number_clikov > 10:
                speed_pers = 5
            else:
                speed_pers = 3
            if number_clikov > 17:
                number_clikov = 0

        board.render(screen)

        # clouds.render()
        treeeeee.render_tree()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
