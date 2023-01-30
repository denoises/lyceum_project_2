import pygame
import sys
import os

pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
clock = pygame.time.Clock()

FPS = 60


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


# walkRight = [load_image('image/low_settings/person/right/right0001.png'),
#              load_image('image/low_settings/person/right/right0002.png'),
#              load_image('image/low_settings/person/right/right0003.png'),
#              load_image('image/low_settings/person/right/right0004.png'),
#              load_image('image/low_settings/person/right/right0005.png'),
#              load_image('image/low_settings/person/right/right0006.png'),
#              load_image('image/low_settings/person/right/right0007.png'),
#              load_image('image/low_settings/person/right/right0008.png'),
#              load_image('image/low_settings/person/right/right0009.png'),
#              load_image('image/low_settings/person/right/right0010.png'),
#              load_image('image/low_settings/person/right/right0011.png'),
#              load_image('image/low_settings/person/right/right0012.png'),
#              load_image('image/low_settings/person/right/right0013.png'),
#              load_image('image/low_settings/person/right/right0014.png'),
#              load_image('image/low_settings/person/right/right0015.png'),
#              load_image('image/low_settings/person/right/right0016.png'),
#              load_image('image/low_settings/person/right/right0017.png'),
#              load_image('image/low_settings/person/right/right0018.png'),
#              load_image('image/low_settings/person/right/right0019.png'),
#              load_image('image/low_settings/person/right/right0020.png'),
#              load_image('image/low_settings/person/right/right0021.png'),
#              load_image('image/low_settings/person/right/right0022.png'),
#              load_image('image/low_settings/person/right/right0023.png'),
#              load_image('image/low_settings/person/right/right0024.png'),
#              load_image('image/low_settings/person/right/right0025.png'),
#              load_image('image/low_settings/person/right/right0026.png'),
#              load_image('image/low_settings/person/right/right0027.png'),
#              load_image('image/low_settings/person/right/right0028.png'),
#              load_image('image/low_settings/person/right/right0029.png'),
#              load_image('image/low_settings/person/right/right0030.png'),
#              load_image('image/low_settings/person/right/right0031.png'),
#              load_image('image/low_settings/person/right/right0032.png'),
#              load_image('image/low_settings/person/right/right0033.png'),
#              load_image('image/low_settings/person/right/right0034.png'),
#              load_image('image/low_settings/person/right/right0035.png'),
#              load_image('image/low_settings/person/right/right0036.png'),
#              load_image('image/low_settings/person/right/right0037.png'),
#              load_image('image/low_settings/person/right/right0038.png'),
#              load_image('image/low_settings/person/right/right0039.png'),
#              load_image('image/low_settings/person/right/right0040.png'),
#              load_image('image/low_settings/person/right/right0041.png'),
#              load_image('image/low_settings/person/right/right0042.png'),
#              load_image('image/low_settings/person/right/right0043.png'),
#              load_image('image/low_settings/person/right/right0044.png'),
#              load_image('image/low_settings/person/right/right0045.png'),
#              load_image('image/low_settings/person/right/right0046.png'),
#              load_image('image/low_settings/person/right/right0047.png'),
#              load_image('image/low_settings/person/right/right0048.png'),
#              load_image('image/low_settings/person/right/right0049.png'),
#              load_image('image/low_settings/person/right/right0050.png'),
#              ]


# animCount = 0
#
# width_pers = 100
# height_pers = 100
# left = False
# right = False
# up = False
# down = False
# speed_pers = 5
# x_pers = 500
# y_pers = 500
# run = True
#
# # while run:
#     # pygame.time.delay()
#     clock.tick(50)
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         x_pers -= speed_pers
#         left = True
#         right = False
#         down = False
#         up = False
#     elif keys[pygame.K_RIGHT]:
#         x_pers += speed_pers
#         left = False
#         right = True
#         up = False
#         down = False
#     else:
#         left = False
#         right = False
#         up = False
#         down = False
#         animCount = 0


def main():  # исование основного окна

    # global animCount  # анимация персонажа

    size = width, height = 1920, 1080
    start_screen()
    # level_map = load_level('map.map')
    # hero, max_x, max_y = generate_level(level_map)
    running = True
    start = True
    man = None
    x = 0
    f = True

    screen = pygame.display.set_mode(size)

    # КУРСОР
    image_cursor = load_image('image/navigate.png')
    image_cur = pygame.transform.scale(image_cursor, (25, 25))
    cursor = pygame.sprite.Sprite()
    cursor.image = image_cur
    cursor.rect = cursor.image.get_rect()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(cursor)
    pygame.mouse.set_visible(False)



    while running:
        if x + 200 > 500:
            f = False
        elif x < 0:
            f = True
        if f:
            x -= 0.25
        else:
            x -= 0.25

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                cursor.rect.topleft = event.pos
            all_sprites.update(event)
        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(50)
        # if animCount + 1 >= 50:  # фотки кончились - пора повторять!
        #     animCount = 0

        # if right:
        #     screen.blit(walkRight[animCount // 5], (x_pers, y_pers))
        #     animCount += 1
        # elif left:
        #     pass
        pygame.display.flip()

    pygame.quit()


main()
