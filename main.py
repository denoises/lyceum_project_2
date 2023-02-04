import random

import pygame

from map_generate import Tree_class, Board
from start_screen_and_cursor import start_screen
from weather import Light

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

        # right
        self.images_person_right = [pygame.image.load(f"image/low_settings/person/right/right00{i:02d}.png") for i in
                                    range(1, 50)]
        # left
        self.images_person_left = [pygame.image.load(f"image/low_settings/person/left/left00{i:02d}.png") for i in
                                   range(1, 50)]
        # up
        self.images_person_up = [pygame.image.load(f"image/low_settings/person/up/up00{i:02d}.png") for i in
                                 range(1, 50)]
        # down
        self.images_person_down = [pygame.image.load(f"image/low_settings/person/down/down00{i:02d}.png") for i in
                                   range(1, 50)]
        # left_up
        self.images_person_left_up = [pygame.image.load(f"image/low_settings/person/left up/left_up00{i:02d}.png") for i
                                      in
                                      range(1, 50)]
        # left_down
        self.images_person_left_down = [pygame.image.load(f"image/low_settings/person/left down/left_down00{i:02d}.png")
                                        for i in
                                        range(1, 50)]
        # right_up
        self.images_person_right_up = [pygame.image.load(f"image/low_settings/person/right up/right_up00{i:02d}.png")
                                       for i in
                                       range(1, 50)]
        # right_down
        self.images_person_right_down = [
            pygame.image.load(f"image/low_settings/person/right down/right_down00{i:02d}.png") for i in
            range(1, 50)]

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
        pygame.display.set_mode()
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
