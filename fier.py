import pygame



SIZE = WIDTH, HEIGHT = 600, 400
BACKGROUND_COLOR = pygame.Color((0, 0, 0))
FPS = 10


class anim_fire(pygame.sprite.Sprite):
    def __init__(self):
        super(anim_fire, self).__init__()

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

        self.image = pygame.transform.scale(self.fire_image[self.index], (10, 10))

        self.rect = pygame.Rect(5, 5, 400, 198)

    def update(self):
        self.index += 1

        if self.index >= len(self.fire_image):
            self.index = 0

        self.image = self.fire_image[self.index]


def main():

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = anim_fire()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        my_group.update()
        screen.fill(BACKGROUND_COLOR)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
