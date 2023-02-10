import random
import sqlite3
import pygame

from map_generate import Tree_class, Board
from start_screen_and_cursor import start_screen
from weather import Light
from person import Person
from fire import Fire
from timer import Timer
from final_screen import Final
from load_image import load_image

pygame.init()
size = width, height = 1920, 1080
which_way = 'down'
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
clock = pygame.time.Clock()

scores = 1000  # баллы 1000 стандарт

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
    pp = 0
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

    f = open('nickname.txt', mode='r', encoding='utf-8')
    name_player = f.readlines()[0]
    print(name_player)
    aaa = 0
    board = Board(18, 9)
    col_p_pl = 0
    # clouds = Clouds()
    fire_cl = Fire()
    board.set_view(0, 0, 150)
    treeeeee = Tree_class(0, 1920, 1080, 0)
    treeeeee.tree(screen)
    light_cl = Light()
    n_a_p = 0
    running = True
    pygame.init()
    player_take_anim = False
    player_throw_anim = False
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
                    and event.key == pygame.K_r):
                main()
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
                        x_rect = Person.rendering.x_coodr_person_rect
                        y_rect = Person.rendering.y_coodr_person_rect
                        print('spase')
                        print(x, y)
                        treeeeee.col_proverka(x, y, x_rect, y_rect)
                        col_p_pl__1 = Tree_class.col_proverka.col_p_pl
                        if col_p_pl__1 == 1:
                            player_take_anim = True
                    elif el_in_the_hands == 1:
                        x = Person.rendering.x_coodr_person_osn
                        y = Person.rendering.y_coodr_person_osn
                        x_rect = Person.rendering.x_coodr_person_rect
                        y_rect = Person.rendering.y_coodr_person_rect
                        fire_cl.colizion_f(x, y, x_rect, y_rect)
                        f = Fire.colizion_f.eeee_proverka_col_fire
                        print(f)
                        if f == 1:
                            print('in fire colizion')
                            player_throw_anim = True
                            scores += 40

            # что то на подобии ускорения, нужно допиливать
            if number_clikov > 10:
                speed_pers = 15
            else:
                speed_pers = 5
            if number_clikov > 17:
                number_clikov = 0

        board.render(screen)

        my_group_for_fire.update()  # АААА горим

        # незнаю как лучше, кгода персонаж ходит по ёлкам или ёлки по персонажу
        player.rendering()

        if player_take_anim == True:  # анимка взятия
            n_a_p += 1
            player.take_el(which_way)
            if n_a_p >= 9:
                n_a_p = 0
                player_take_anim = False

        if player_throw_anim == True:  # анимка кидания
            n_a_p += 1
            player.throw_el(which_way)
            if n_a_p >= 9:
                n_a_p = 0
                player_throw_anim = False

        treeeeee.render_tree()
        # clouds.render()

        if scores < 850:
            light_cl.render_10()
        if scores < 650:
            light_cl.render_20()
        if scores < 550:
            light_cl.render_30()
        if scores < 300:
            light_cl.render_40()
        if scores < 160:
            light_cl.render_50()
        if scores < 80:
            light_cl.render_80()

        if scores <= 0 and pp != 1:
            light_cl.render_100()
            print('GG')
            gg_s = pygame.mixer.Sound('other/sounds/gg.mp3')
            gg_s.play()

            con = sqlite3.connect('bd/BD_for_axmans.db')
            cursor = con.cursor()
            my_time = Timer.mytime
            print(my_time)
            ff = cursor.execute(f""" INSERT INTO players_score(name, time) VALUES(?, ?)""",
                                (f'{str(name_player)}', f'{str(my_time)}'))
            pp = 1
            con.commit()
            con.close()
            aaa = 1

        if aaa == 1:
            Final()

        scores_game()
        Timer()
        pygame.display.flip()
        if scores > 0:
            scores -= 1
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
