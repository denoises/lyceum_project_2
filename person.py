import pygame
import sys

which_way = 'up'

pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
clock = pygame.time.Clock()


class Person(pygame.sprite.Sprite):  # маленький лесорубик
    def __init__(self):
        super(Person, self).__init__()

        self.index = 0
        self.x = 800
        self.y = 500
        self.speed_pers = 5

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

    def update(self, which_way, speed_pers):
        self.which_way = which_way
        self.speed_pers = speed_pers
        if self.which_way == 'up':
            self.images_person_now = self.images_person_up
            self.y -= self.speed_pers
        elif self.which_way == 'down':
            self.y += self.speed_pers
            self.images_person_now = self.images_person_down
        elif self.which_way == 'left':
            self.x -= self.speed_pers
            self.images_person_now = self.images_person_left
        elif self.which_way == 'right':
            self.x += self.speed_pers
            self.images_person_now = self.images_person_right
        else:
            self.images_person_now = self.images_person_down  # стандарт


        if self.speed_pers == 3:
            self.index += 1
        elif self.speed_pers == 5:
            self.index += 2
        elif self.speed_pers == 10:
            self.index += 4
        elif self.speed_pers == 15:
            self.index += 6

        if self.index >= len(self.images_person_now):
            self.index = 0

    def rendering(self):
        self.image_pers = pygame.transform.scale(self.images_person_now[self.index], (300, 300))
        screen.blit(self.image_pers, (self.x, self.y))


def main():
    global which_way
    which_way = 'down'
    speed_pers = 5
    running = True
    start = False
    pygame.init()
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)

    player = Person()
    player.update(which_way, speed_pers)

    pygame.mouse.set_visible(False)
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_UP):
                which_way = 'up'
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_DOWN):
                which_way = 'down'
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_LEFT):
                which_way = 'left'
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_RIGHT):
                which_way = 'right'

            player.update(which_way, speed_pers)

        player.rendering()

        clock.tick(60)
        pygame.display.update()
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
