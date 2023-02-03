import pygame
import os
import sys
import random
from load_image import load_image
from start_screen_and_cursor import start_screen
from weather import Light, Clouds
from map_generate import Tree_class, Board

pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
clock = pygame.time.Clock()

scores = 1000  # баллы

rand_gen_for_patern = [random.randint(0, 9) for i in range(162)]
rand_gen_for_clouds = int(random.randint(0, 10))


# 1000 очков всего, за каждые 500 милисикунд  - 7 очков
# одно срубленное дерево, кинутое в костёр + 50 очков
# удачи

# ПЕРСОНАЖ, тут только список анимаций и кривая логика обновления спрайтов
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


# Класс огня, тут просто отрисовываются спрайты огня, ДОРАБАТЫВАТЬ
class Fire(pygame.sprite.Sprite):  # костёр
    def __init__(self):
        super(Fire, self).__init__()
        background = pygame.display.set_mode()
        self.fire_image = [pygame.image.load('image/low_settings/fire/fire0018.png'),
                           pygame.image.load('image/low_settings/fire/fire0019.png'),
                           pygame.image.load('image/low_settings/fire/fire0020.png'),
                           pygame.image.load('image/low_settings/fire/fire0021.png'),
                           pygame.image.load('image/low_settings/fire/fire0022.png'),
                           pygame.image.load('image/low_settings/fire/fire0023.png'),
                           pygame.image.load('image/low_settings/fire/fire0024.png'),
                           pygame.image.load('image/low_settings/fire/fire0025.png'),
                           pygame.image.load('image/low_settings/fire/fire0026.png'),
                           pygame.image.load('image/low_settings/fire/fire0027.png'),
                           pygame.image.load('image/low_settings/fire/fire0028.png'),
                           pygame.image.load('image/low_settings/fire/fire0029.png'),
                           pygame.image.load('image/low_settings/fire/fire0030.png'),
                           pygame.image.load('image/low_settings/fire/fire0031.png'),
                           pygame.image.load('image/low_settings/fire/fire0032.png'),
                           pygame.image.load('image/low_settings/fire/fire0033.png'),
                           pygame.image.load('image/low_settings/fire/fire0034.png'),
                           pygame.image.load('image/low_settings/fire/fire0035.png'),
                           pygame.image.load('image/low_settings/fire/fire0036.png'),
                           pygame.image.load('image/low_settings/fire/fire0037.png'),
                           pygame.image.load('image/low_settings/fire/fire0038.png'),
                           pygame.image.load('image/low_settings/fire/fire0039.png'),
                           pygame.image.load('image/low_settings/fire/fire0040.png'),
                           pygame.image.load('image/low_settings/fire/fire0041.png'),
                           pygame.image.load('image/low_settings/fire/fire0042.png'),
                           pygame.image.load('image/low_settings/fire/fire0043.png'),
                           pygame.image.load('image/low_settings/fire/fire0044.png'),
                           pygame.image.load('image/low_settings/fire/fire0045.png'),
                           pygame.image.load('image/low_settings/fire/fire0046.png'),
                           pygame.image.load('image/low_settings/fire/fire0047.png'),
                           pygame.image.load('image/low_settings/fire/fire0048.png'),
                           pygame.image.load('image/low_settings/fire/fire0049.png'),
                           pygame.image.load('image/low_settings/fire/fire0050.png'),
                           pygame.image.load('image/low_settings/fire/fire0061.png'),
                           pygame.image.load('image/low_settings/fire/fire0062.png'),
                           pygame.image.load('image/low_settings/fire/fire0063.png'),
                           pygame.image.load('image/low_settings/fire/fire0064.png'),
                           pygame.image.load('image/low_settings/fire/fire0065.png'),
                           pygame.image.load('image/low_settings/fire/fire0066.png'),
                           pygame.image.load('image/low_settings/fire/fire0067.png'),
                           pygame.image.load('image/low_settings/fire/fire0068.png'),
                           pygame.image.load('image/low_settings/fire/fire0069.png'),
                           pygame.image.load('image/low_settings/fire/fire0070.png')

                           ]
        self.index = 0
        self.rect = pygame.Rect(5, 5, 400, 198)

    def update(self):
        self.index += 1

        if self.index >= len(self.fire_image):
            self.index = 0

        self.image = pygame.transform.scale(self.fire_image[self.index], (400, 400))
        screen.blit(self.image, (790, 370))


def main():
    screen = pygame.display.set_mode(size)
    pygame.mixer.music.load("other/sounds/fon.mp3")
    pygame.mixer.music.play(-1)
    start_screen()

    my_sprite_for_fire = Fire()
    my_group_for_fire = pygame.sprite.Group(my_sprite_for_fire)

    sprite_for_light = Light()
    group_for_light = pygame.sprite.Group(sprite_for_light)

    board = Board(18, 9)
    # clouds = Clouds()

    board.set_view(0, 0, 150)
    treeeeee = Tree_class(0, 1920, 1080, 0)

    running = True
    pygame.init()

    run_gr = True
    while run_gr:
        treeeeee.tree(screen)
        run_gr = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # ТУТ КНОПКИ ПЕРСОНАЖ И ТП

        board.render(screen)

        my_group_for_fire.update()  # АААА горим
        group_for_light.update()
        # clouds.render()
        treeeeee.tree(screen)
        pygame.display.flip()
        clock.tick(120)
    pygame.quit()


if __name__ == '__main__':
    main()
