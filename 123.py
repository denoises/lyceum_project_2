import pygame
import sys
import os


# ДОДЕЛАТЬ

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


def main():
    running = True
    start = False
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    person_sprite = Person()
    my_group = pygame.sprite.Group(person_sprite)

    image = load_image('img/arrow.png')
    image1 = load_image('img/creature.png', colorkey='#FFFFFF')


    cursor = pygame.sprite.Sprite()
    hero = pygame.sprite.Sprite()
    hero.image = image1
    hero.rect = cursor.image.get_rect()
    cursor.image = image
    cursor.rect = cursor.image.get_rect()
    all_sprites = pygame.sprite.Group()

    all_sprites.add(hero)
    all_sprites.add(cursor)

    pygame.mouse.set_visible(False)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if (event.type == pygame.KETDOWN
                    and event.ket == pygame.K_SPACE):
                start = not start
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_UP):
                hero.rect.top -= 10
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_DOWN):
                hero.rect.top += 10
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_LEFT):
                hero.rect.left += 10
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_RIGHT):
                hero.rect.left -= 10

            if event.type == pygame.MOUSEMOTION:
                cursor.rect.topleft = event.pos
            screen.fill('#000000')
            all_sprites.draw(screen)
            pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
