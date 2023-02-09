import pygame
from person import Person

size = width, height = 1920, 1080
which_way = 'down'
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
clock = pygame.time.Clock()


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
        self.proverka_col_fire = 0
        Fire.colizion_f.eeee_proverka_col_fire = self.proverka_col_fire

    def update(self):
        self.index += 1

        if self.index >= len(self.fire_image):
            self.index = 0

        self.image = pygame.transform.scale(self.fire_image[self.index], (400, 400))
        screen.blit(self.image, (790, 370))

    def colizion_f(self, x, y):
        self.proverka_col_fire = 0
        Fire.colizion_f.eeee_proverka_col_fire = self.proverka_col_fire
        self.x_coord_person = x
        self.y_coord_person = y
        fire_rect = pygame.Rect(900, 420, 50, 50)
        pers_rect = pygame.image.load(
            f"image/low_settings/person_take-throw/down/person_take-throw_down0001.png").get_rect(
            topleft=(self.x_coord_person, self.y_coord_person))
        collide_p_f = pygame.Rect.colliderect(fire_rect, pers_rect)
        if collide_p_f:
            sound_of_taking()
            self.proverka_col_fire = 1
            Fire.colizion_f.eeee_proverka_col_fire = self.proverka_col_fire


def sound_of_taking():
    take_s = pygame.mixer.Sound('other/sounds/take-throw.mp3')
    take_s.play()
