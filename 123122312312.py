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

FPS = 60


class Board:
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
        sp_ground = (pygame.image.load('image/low_settings/ground/ground0000.png').convert_alpha(),
                     pygame.image.load('image/low_settings/ground/ground0001.png').convert_alpha(),
                     pygame.image.load('image/low_settings/ground/ground0002.png').convert_alpha(),
                     pygame.image.load('image/low_settings/ground/ground0003.png').convert_alpha(),
                     pygame.image.load('image/low_settings/ground/ground0004.png').convert_alpha(),
                     pygame.image.load('image/low_settings/ground/ground0005.png').convert_alpha(),
                     pygame.image.load('image/low_settings/ground/ground0006.png').convert_alpha(),
                     pygame.image.load('image/low_settings/ground/ground0007.png').convert_alpha(),
                     pygame.image.load('image/low_settings/ground/ground0008.png').convert_alpha(),
                     pygame.image.load('image/low_settings/ground/ground0009.png').convert_alpha(),
                     )
        for y in range(self.height):
            for x in range(self.width):
                img_ground = sp_ground[random.randint(0, 9)]
                small_img_ground = pygame.transform.scale(img_ground, (150, 150))
                screen.blit(small_img_ground, (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                               self.cell_size, self.cell_size))


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


def main():
    start_screen()
    board = Board(18, 9)
    board.set_view(0, 0, 150)
    running = True
    pygame.init()
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    board.render(screen)
    run_gr = True
    while run_gr:
        board.render(screen)
        run_gr = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # ТУТ КНОПКИ ПЕРСОНАЖ И ТП
            pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
