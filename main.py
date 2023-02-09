import random

import pygame

from map_generate import Tree_class, Board
from start_screen_and_cursor import start_screen
from weather import Light
from person import Person
from fire import Fire
from timer import Timer
from load_image import load_image

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


def scores_game():
    intro_text = (f"{scores}",
                  ""
                  )
    font = pygame.font.Font(None, 30)
    text_coord = 30
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 960
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


def main():
    global which_way, scores
    which_way = 'down'
    speed_pers = 5

    screen = pygame.display.set_mode(size)
    pygame.mixer.music.load("other/sounds/fon.mp3")
    pygame.mixer.music.play(-1)
    start_screen()

    my_sprite_for_fire = Fire()
    my_group_for_fire = pygame.sprite.Group(my_sprite_for_fire)
    number_while = 0
    number_event = 0
    number_clikov = 0

    player = Person()
    player.update(which_way, speed_pers)

    sprite_for_light = Light()
    group_for_light = pygame.sprite.Group(sprite_for_light)

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
                which_way = 'up'
                number_clikov += 1
                player.update(which_way, speed_pers)
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_DOWN):
                which_way = 'down'
                number_clikov += 1
                player.update(which_way, speed_pers)
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_LEFT):
                which_way = 'left'
                number_clikov += 1
                player.update(which_way, speed_pers)
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_RIGHT):
                which_way = 'right'
                number_clikov += 1
                player.update(which_way, speed_pers)
            if event.type == pygame.KEYDOWN:  # Пробел - рубка дерева
                if event.key == pygame.K_SPACE:
                    el_in_the_hands = Person.rendering.elll_in_the_hands
                    if el_in_the_hands == 0:
                        x = Person.rendering.x_coodr_person_osn
                        y = Person.rendering.y_coodr_person_osn
                        print(x, y)
                        treeeeee.col_proverka(x, y)
                        player.take_el(which_way)  # нужно понять как сделать так чтобы оно делалось 10 раз(10 нажатий)
            # что то на подобии ускорения, нужно допиливать
            if number_clikov > 10:
                speed_pers = 15
            else:
                speed_pers = 5
            if number_clikov > 17:
                number_clikov = 0

        board.render(screen)

        my_group_for_fire.update()  # АААА горим

        treeeeee.render_tree()
        # незнаю как лучше, кгода персонаж ходит по ёлкам или ёлки по персонажу
        player.rendering()

        group_for_light.update()
        # clouds.render()

        scores_game()
        Timer()
        pygame.display.flip()
        scores -= 1
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
