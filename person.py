import pygame
import sys


class Person(pygame.sprite.Sprite):  # маленький лесорубик
    def __init__(self, which_way):
        super(Person, self).__init__()

        # right
        self.images_person_right = [pygame.image.load(f"image/low_settings/person/right/right00{i:02d}.png") for i in
                                    range(1, 50)]
        # left
        self.images_person_left = [pygame.image.load(f"image/low_settings/person/left/left00{i:02d}.png") for i in
                                   range(1, 50)]
        # up
        self.images_person_up = [pygame.image.load(f"image/low_settings/person/up/up00{i:02d}.png") for i in
                                 range(1, 50)]
        # down
        self.images_person_down = [pygame.image.load(f"image/low_settings/person/down/down00{i:02d}.png") for i in
                                   range(1, 50)]
        # left_up
        self.images_person_left_up = [pygame.image.load(f"image/low_settings/person/left up/left_up00{i:02d}.png") for i
                                      in
                                      range(1, 50)]
        # left_down
        self.images_person_left_down = [pygame.image.load(f"image/low_settings/person/left down/left_down00{i:02d}.png")
                                        for i in
                                        range(1, 50)]
        # right_up
        self.images_person_right_up = [pygame.image.load(f"image/low_settings/person/right up/right_up00{i:02d}.png")
                                       for i in
                                       range(1, 50)]
        # right_down
        self.images_person_right_down = [
            pygame.image.load(f"image/low_settings/person/right down/right_down00{i:02d}.png") for i in
            range(1, 50)]

        self.images_person_now = self.images_person_left_down
        self.which_way = which_way
        if self.which_way == 'up':
            self.images_person_now = self.images_person_left_down

        self.index = 0

    def update(self):
        self.index += 1

        if self.index >= len(self.images_person_now):
            self.index = 0

        self.image = pygame.transform.scale(self.images_person_right[self.index], (300, 300))
