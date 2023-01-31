import pygame
import os
import sys
import random

pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
clock = pygame.time.Clock()

FPS = 30


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
                img_ground = sp_ground[random.randint(0, 9)]
                small_img_ground = pygame.transform.scale(img_ground, (155, 155))
                screen.blit(small_img_ground, (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                               self.cell_size, self.cell_size))
                # крассота


def load_image(name, colorkey=None):
    fullname = os.path.join('', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    try:
        image = pygame.image.load(fullname)
    except pygame.error as Message:
        print(Message)
        raise SystemExit(Message)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


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
        clock.tick(FPS)


def cursor():  # курсор
    image_cursor = load_image('image/navigate.png')
    image_cur = pygame.transform.scale(image_cursor, (25, 25))
    cursor = pygame.sprite.Sprite()
    cursor.image = image_cur
    cursor.rect = cursor.image.get_rect()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(cursor)
    pygame.mouse.set_visible(False)


class Tree_class:  # это что, елка?
    def __init__(self, min_x_tree, max_x_tree, min_y_tree, max_y_tree):
        self.min_x_tree = min_x_tree
        self.max_x_tree = max_x_tree
        self.min_y_tree = min_y_tree
        self.max_y_tree = max_y_tree

    def tree(self, screen):
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
                if 500 < random_x_cooord < 1100 and 150 < random_y_cooord < 650:  # область без костра
                    proverka = 0
                else:
                    proverka = 1

            screen.blit(tree_image_random_scale,
                        (random_x_cooord, random_y_cooord))  # отрисовка ёлок
            cal_tree_now += 1


class Person(pygame.sprite.Sprite):  # маленький лесорубик
    def __init__(self):
        super(Person, self).__init__()

        self.images_person_right = [pygame.image.load('image/low_settings/person/right/right0001.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0002.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0003.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0004.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0005.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0006.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0007.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0008.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0009.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0010.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0011.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0012.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0013.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0014.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0015.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0016.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0017.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0018.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0019.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0020.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0021.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0022.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0023.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0024.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0025.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0026.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0027.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0028.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0029.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0030.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0031.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0032.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0033.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0034.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0035.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0036.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0037.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0038.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0039.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0040.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0041.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0042.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0043.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0044.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0045.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0046.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0047.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0048.png').convert_alpha(),
                                    pygame.image.load('image/low_settings/person/right/right0049.png').convert_alpha(),
                                    pygame.image.load(
                                        'image/low_settings/person/right/right0050.png').convert_alpha(), ]
        self.images_person_left = [pygame.image.load('image/low_settings/person/left/left0001.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0002.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0003.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0004.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0005.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0006.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0007.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0008.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0009.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0010.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0011.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0012.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0013.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0014.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0015.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0016.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0017.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0018.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0019.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0020.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0021.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0022.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0023.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0024.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0025.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0026.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0027.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0028.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0029.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0030.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0031.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0032.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0033.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0034.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0035.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0036.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0037.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0038.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0039.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0040.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0041.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0042.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0043.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0044.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0045.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0046.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0047.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0048.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0049.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/left/left0050.png').convert_alpha(), ]
        self.images_person_up = [pygame.image.load('image/low_settings/person/up/up0001.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0002.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0003.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0004.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0005.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0006.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0007.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0008.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0009.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0010.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0011.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0012.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0013.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0014.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0015.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0016.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0017.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0018.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0019.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0020.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0021.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0022.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0023.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0024.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0025.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0026.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0027.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0028.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0029.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0020.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0031.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0032.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0033.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0034.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0035.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0036.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0037.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0038.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0039.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0040.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0041.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0042.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0043.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0044.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0045.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0046.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0047.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0048.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0049.png').convert_alpha(),
                                 pygame.image.load('image/low_settings/person/up/up0050.png').convert_alpha()
                                 ]
        self.images_person_down = [pygame.image.load('image/low_settings/person/down/down0001.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0002.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0003.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0004.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0005.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0006.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0007.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0008.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0009.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0010.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0011.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0012.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0013.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0014.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0015.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0016.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0017.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0018.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0019.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0020.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0021.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0022.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0023.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0024.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0025.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0026.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0027.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0028.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0029.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0030.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0031.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0032.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0033.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0034.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0035.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0036.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0037.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0038.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0039.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0040.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0041.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0042.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0043.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0044.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0045.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0046.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0047.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0048.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0049.png').convert_alpha(),
                                   pygame.image.load('image/low_settings/person/down/down0050.png').convert_alpha(),
                                   ]
        #  мне кажется был вариант полегче, чем все это в ручную писать, но уже поздно
        self.index = 0
        self.rect = pygame.Rect(5, 5, 400, 198)

    def update(self):
        self.index += 1

        if self.index >= len(self.images_person_right):
            self.index = 0

        self.image = pygame.transform.scale(self.images_person_right[self.index], (300, 300))


class Fire(pygame.sprite.Sprite):  # костёр
    def __init__(self):
        super(Fire, self).__init__()
        self.fire_image = [pygame.image.load('image/low_settings/fire/fire0018.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0019.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0020.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0021.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0022.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0023.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0024.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0025.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0026.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0027.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0028.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0029.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0030.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0031.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0032.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0033.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0034.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0035.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0036.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0037.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0038.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0039.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0040.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0041.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0042.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0043.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0044.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0045.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0046.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0047.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0048.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0049.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0050.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0061.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0062.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0063.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0064.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0065.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0066.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0067.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0068.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0069.png').convert_alpha(),
                           pygame.image.load('image/low_settings/fire/fire0070.png').convert_alpha(),

                           ]
        self.index = 0
        self.rect = pygame.Rect(5, 5, 400, 198)

    def update(self):
        self.index += 1

        if self.index >= len(self.fire_image):
            self.index = 0

        self.image = pygame.transform.scale(self.fire_image[self.index], (300, 300))
        screen.blit(self.image, (850, 450))


def main():
    start_screen()
    my_sprite_for_fire = Fire()
    my_group_for_fire = pygame.sprite.Group(my_sprite_for_fire)
    board = Board(18, 9)

    board.set_view(0, 0, 150)
    treeeeee = Tree_class(0, 1920, 1080, 0)

    running = True
    pygame.init()
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    run_gr = True
    while run_gr:
        board.render(screen)
        treeeeee.tree(screen)
        run_gr = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # ТУТ КНОПКИ ПЕРСОНАЖ И ТП

            pygame.display.flip()
        my_group_for_fire.update()  # АААА горим
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
