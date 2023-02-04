import random

import pygame

from map_generate import Tree_class, Board
from start_screen_and_cursor import start_screen
from weather import Light
from person import Person
from fire import Fire

pygame.init()
size = width, height = 1920, 1080
which_way = 'down'
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

def main():
    global which_way
    which_way = 'down'
    speed_pers = 5

    screen = pygame.display.set_mode(size)
    pygame.mixer.music.load("other/sounds/fon.mp3")
    pygame.mixer.music.play(-1)
    start_screen()

    my_sprite_for_fire = Fire()
    my_group_for_fire = pygame.sprite.Group(my_sprite_for_fire)

    player = Person()
    player.update(which_way, speed_pers)

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
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_UP):
                which_way = 'up'
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_DOWN):
                which_way = 'down'
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_LEFT):
                which_way = 'left'
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_RIGHT):
                which_way = 'right'

            player.update(which_way, speed_pers)


            # ТУТ КНОПКИ ПЕРСОНАЖ И ТП

        board.render(screen)

        my_group_for_fire.update()  # АААА горим
        player.rendering()
        group_for_light.update()
        # clouds.render()
        treeeeee.tree(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
