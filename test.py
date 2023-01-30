import pygame
from pygame.locals import *

pygame.init()


class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()

        self.FPS = 60
        self.x = 100
        self.y = 100
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.person_speed = 20
        self.run = True
        self.animCount = 0

        self.rect = pygame.Rect(5, 5, 150, 198)
        pygame.display.set_caption('AxeMan')

        # image = [pygame.image.load(r'image/low_settings/person/right/right0001.png'),
        #          pygame.image.load(r'image/low_settings/person/left/left0001.png')]
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
        self.images_person_left = [pygame.image.load('image/low_settings/person/left/left0001.png'),
                                   pygame.image.load('image/low_settings/person/left/left0002.png'),
                                   pygame.image.load('image/low_settings/person/left/left0003.png'),
                                   pygame.image.load('image/low_settings/person/left/left0004.png'),
                                   pygame.image.load('image/low_settings/person/left/left0005.png'),
                                   pygame.image.load('image/low_settings/person/left/left0006.png'),
                                   pygame.image.load('image/low_settings/person/left/left0007.png'),
                                   pygame.image.load('image/low_settings/person/left/left0008.png'),
                                   pygame.image.load('image/low_settings/person/left/left0009.png'),
                                   pygame.image.load('image/low_settings/person/left/left0010.png'),
                                   pygame.image.load('image/low_settings/person/left/left0011.png'),
                                   pygame.image.load('image/low_settings/person/left/left0012.png'),
                                   pygame.image.load('image/low_settings/person/left/left0013.png'),
                                   pygame.image.load('image/low_settings/person/left/left0014.png'),
                                   pygame.image.load('image/low_settings/person/left/left0015.png'),
                                   pygame.image.load('image/low_settings/person/left/left0016.png'),
                                   pygame.image.load('image/low_settings/person/left/left0017.png'),
                                   pygame.image.load('image/low_settings/person/left/left0018.png'),
                                   pygame.image.load('image/low_settings/person/left/left0019.png'),
                                   pygame.image.load('image/low_settings/person/left/left0020.png'),
                                   pygame.image.load('image/low_settings/person/left/left0021.png'),
                                   pygame.image.load('image/low_settings/person/left/left0022.png'),
                                   pygame.image.load('image/low_settings/person/left/left0023.png'),
                                   pygame.image.load('image/low_settings/person/left/left0024.png'),
                                   pygame.image.load('image/low_settings/person/left/left0025.png'),
                                   pygame.image.load('image/low_settings/person/left/left0026.png'),
                                   pygame.image.load('image/low_settings/person/left/left0027.png'),
                                   pygame.image.load('image/low_settings/person/left/left0028.png'),
                                   pygame.image.load('image/low_settings/person/left/left0029.png'),
                                   pygame.image.load('image/low_settings/person/left/left0030.png'),
                                   pygame.image.load('image/low_settings/person/left/left0031.png'),
                                   pygame.image.load('image/low_settings/person/left/left0032.png'),
                                   pygame.image.load('image/low_settings/person/left/left0033.png'),
                                   pygame.image.load('image/low_settings/person/left/left0034.png'),
                                   pygame.image.load('image/low_settings/person/left/left0035.png'),
                                   pygame.image.load('image/low_settings/person/left/left0036.png'),
                                   pygame.image.load('image/low_settings/person/left/left0037.png'),
                                   pygame.image.load('image/low_settings/person/left/left0038.png'),
                                   pygame.image.load('image/low_settings/person/left/left0039.png'),
                                   pygame.image.load('image/low_settings/person/left/left0040.png'),
                                   pygame.image.load('image/low_settings/person/left/left0041.png'),
                                   pygame.image.load('image/low_settings/person/left/left0042.png'),
                                   pygame.image.load('image/low_settings/person/left/left0043.png'),
                                   pygame.image.load('image/low_settings/person/left/left0044.png'),
                                   pygame.image.load('image/low_settings/person/left/left0045.png'),
                                   pygame.image.load('image/low_settings/person/left/left0046.png'),
                                   pygame.image.load('image/low_settings/person/left/left0047.png'),
                                   pygame.image.load('image/low_settings/person/left/left0048.png'),
                                   pygame.image.load('image/low_settings/person/left/left0049.png'),
                                   pygame.image.load('image/low_settings/person/left/left0050.png'), ]

        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        self.animCount += 1

        if self.animCount >= 50:
            self.animCount = 0

        self.images_person_right_im = self.images_person_right[self.animCount]
        self.images_person_left_im = self.images_person_left[self.animCount]

    def main(self):
        direction = True
        window = pygame.display.set_mode((1920, 1080))
        clock = pygame.time.Clock()

        my_sprite = MySprite()
        my_group = pygame.sprite.Group(my_sprite)

        clock.tick(self.FPS)
        window.fill((255, 255, 255))

        while run:
            if direction == True:
                window.blit(self.images_person_right_im, (self.x, self.y))
            if direction == False:
                window.blit(self.images_person_left_im, (self.x, self.y))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        direction = True
                    elif event.key == pygame.K_LEFT:
                        direction = False
            key_pressed_is = pygame.key.get_pressed()
            if key_pressed_is[K_LEFT] and self.x >= -40:
                self.x -= self.person_speed
            if key_pressed_is[K_RIGHT] and self.x <= 1700:
                self.x += self.person_speed
            if key_pressed_is[K_UP] and self.y > -100:
                self.y -= self.person_speed
            if key_pressed_is[K_DOWN] and self.y < 970:
                self.y += self.person_speed

            my_group.update()
            my_group.draw(window)
            pygame.display.update()
