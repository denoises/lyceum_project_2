import pygame

SIZE = WIDTH, HEIGHT = 600, 400
BACKGROUND_COLOR = pygame.Color((0, 0, 0))
FPS = 30


class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()

        self.images_person_right = [pygame.image.load('image/low_settings/person/right/right0001.png'),
                                    pygame.image.load('image/low_settings/person/right/right0002.png'),
                                    pygame.image.load('image/low_settings/person/right/right0003.png'),
                                    pygame.image.load('image/low_settings/person/right/right0004.png'),
                                    pygame.image.load('image/low_settings/person/right/right0005.png'),
                                    pygame.image.load('image/low_settings/person/right/right0006.png'),
                                    pygame.image.load('image/low_settings/person/right/right0007.png'),
                                    pygame.image.load('image/low_settings/person/right/right0008.png'),
                                    pygame.image.load('image/low_settings/person/right/right0009.png'),
                                    pygame.image.load('image/low_settings/person/right/right0010.png'),
                                    pygame.image.load('image/low_settings/person/right/right0011.png'),
                                    pygame.image.load('image/low_settings/person/right/right0012.png'),
                                    pygame.image.load('image/low_settings/person/right/right0013.png'),
                                    pygame.image.load('image/low_settings/person/right/right0014.png'),
                                    pygame.image.load('image/low_settings/person/right/right0015.png'),
                                    pygame.image.load('image/low_settings/person/right/right0016.png'),
                                    pygame.image.load('image/low_settings/person/right/right0017.png'),
                                    pygame.image.load('image/low_settings/person/right/right0018.png'),
                                    pygame.image.load('image/low_settings/person/right/right0019.png'),
                                    pygame.image.load('image/low_settings/person/right/right0020.png'),
                                    pygame.image.load('image/low_settings/person/right/right0021.png'),
                                    pygame.image.load('image/low_settings/person/right/right0022.png'),
                                    pygame.image.load('image/low_settings/person/right/right0023.png'),
                                    pygame.image.load('image/low_settings/person/right/right0024.png'),
                                    pygame.image.load('image/low_settings/person/right/right0025.png'),
                                    pygame.image.load('image/low_settings/person/right/right0026.png'),
                                    pygame.image.load('image/low_settings/person/right/right0027.png'),
                                    pygame.image.load('image/low_settings/person/right/right0028.png'),
                                    pygame.image.load('image/low_settings/person/right/right0029.png'),
                                    pygame.image.load('image/low_settings/person/right/right0030.png'),
                                    pygame.image.load('image/low_settings/person/right/right0031.png'),
                                    pygame.image.load('image/low_settings/person/right/right0032.png'),
                                    pygame.image.load('image/low_settings/person/right/right0033.png'),
                                    pygame.image.load('image/low_settings/person/right/right0034.png'),
                                    pygame.image.load('image/low_settings/person/right/right0035.png'),
                                    pygame.image.load('image/low_settings/person/right/right0036.png'),
                                    pygame.image.load('image/low_settings/person/right/right0037.png'),
                                    pygame.image.load('image/low_settings/person/right/right0038.png'),
                                    pygame.image.load('image/low_settings/person/right/right0039.png'),
                                    pygame.image.load('image/low_settings/person/right/right0040.png'),
                                    pygame.image.load('image/low_settings/person/right/right0041.png'),
                                    pygame.image.load('image/low_settings/person/right/right0042.png'),
                                    pygame.image.load('image/low_settings/person/right/right0043.png'),
                                    pygame.image.load('image/low_settings/person/right/right0044.png'),
                                    pygame.image.load('image/low_settings/person/right/right0045.png'),
                                    pygame.image.load('image/low_settings/person/right/right0046.png'),
                                    pygame.image.load('image/low_settings/person/right/right0047.png'),
                                    pygame.image.load('image/low_settings/person/right/right0048.png'),
                                    pygame.image.load('image/low_settings/person/right/right0049.png'),
                                    pygame.image.load('image/low_settings/person/right/right0050.png'), ]

        self.index = 0

        self.image = self.images_person_right[self.index]

        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        self.index += 1

        if self.index >= len(self.images_person_right):
            self.index = 0

        self.image = self.images_person_right[self.index]


def main():
    running = True
    start = False
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()
    x_pers = 10
    y_pers = 10
    speed_pers = 5
    hero = pygame.sprite.Sprite()

    all_sprites = pygame.sprite.Group()

    all_sprites.add(hero)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_SPACE):
                start = not start
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_UP):
                y_pers -= speed_pers
                print('K_UP')
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_DOWN):
                y_pers += speed_pers
                print('K_DOWN')
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_LEFT):
                x_pers -= speed_pers
                print('K_LEFT')
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_RIGHT):
                x_pers += speed_pers
                print('K_RIGHT')


        my_group.update()
        screen.fill(BACKGROUND_COLOR)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
