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
        self.x_coodr_person_osn = 800
        self.y_coodr_person_osn = 500
        self.speed_pers = 5
        self.take = 0  # если 1 то в данный момент берёт елку
        self.in_the_hands = 0  # если 1 то несёт елуку
        self.throw = 0  # если 1 то кидает елуку в костёр
        self.index_take = 0
        self.index_throw = 0

        #
        #
        # ХОДИТ И ДУМАЕТ ЧТО СВОРОВАТЬ:
        #
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
        #
        #
        #
        # ВОРУЕТ ДЕРЕВО:
        #
        self.images_person_take_throw_down = [
            pygame.image.load(f"image/low_settings/person_take-throw/down/person_take-throw_down{i:04d}.png") for i in
            range(1, 10)]
        self.images_person_take_throw_right = [
            pygame.image.load(f"image/low_settings/person_take-throw/right/person_take-throw_right{i:04d}.png") for i in
            range(1, 10)]
        self.images_person_take_throw_left = [
            pygame.image.load(f"image/low_settings/person_take-throw/left/person_take-throw_left{i:04d}.png") for i in
            range(1, 10)]
        self.images_person_take_throw_up = [
            pygame.image.load(f"image/low_settings/person_take-throw/up/person_take-throw_up{i:04d}.png") for i in
            range(1, 10)]
        #
        #
        #
        # УКРАЛ ДЕРЕВО, и радостно бежит:
        #
        self.images_person_with_tree_right = [
            pygame.image.load(f"image/low_settings/person_with_tree/right/person_with_tree_right{i:04d}.png") for i in
            range(1, 50)]
        self.images_person_with_tree_left = [
            pygame.image.load(f"image/low_settings/person_with_tree/left/person_with_tree_left{i:04d}.png") for i in
            range(1, 50)]
        self.images_person_with_tree_up = [
            pygame.image.load(f"image/low_settings/person_with_tree/up/person_with_tree_up{i:04d}.png") for i in
            range(1, 50)]
        self.images_person_with_tree_down = [
            pygame.image.load(f"image/low_settings/person_with_tree/down/person_with_tree_down{i:04d}.png") for i in
            range(1, 50)]
        #
        #
        #

    def update(self, which_way, speed_pers):
        self.which_way = which_way
        self.speed_pers = speed_pers
        if self.in_the_hands == 0:
            if self.which_way == 'up':
                self.images_person_now = self.images_person_up
                self.y_coodr_person_osn -= self.speed_pers
            elif self.which_way == 'down':
                self.y_coodr_person_osn += self.speed_pers
                self.images_person_now = self.images_person_down
            elif self.which_way == 'left':
                self.x_coodr_person_osn -= self.speed_pers
                self.images_person_now = self.images_person_left
            elif self.which_way == 'right':
                self.x_coodr_person_osn += self.speed_pers
                self.images_person_now = self.images_person_right
            elif self.which_way == 'right_up':
                self.x_coodr_person_osn += self.speed_pers
                self.images_person_now = self.images_person_right_up
            elif self.which_way == 'right_down':
                self.x_coodr_person_osn += self.speed_pers
                self.images_person_now = self.images_person_right_down
            elif self.which_way == 'left_up':
                self.x_coodr_person_osn -= self.speed_pers
                self.images_person_now = self.images_person_left_up
            elif self.which_way == 'left_down':
                self.x_coodr_person_osn -= self.speed_pers
                self.images_person_now = self.images_person_left_down
            else:
                self.images_person_now = self.images_person_down  # стандарт
        else:
            if self.which_way == 'up':
                self.images_person_now = self.images_person_with_tree_up
                self.y_coodr_person_osn -= self.speed_pers
            elif self.which_way == 'down':
                self.y_coodr_person_osn += self.speed_pers
                self.images_person_now = self.images_person_with_tree_down
            elif self.which_way == 'left':
                self.x_coodr_person_osn -= self.speed_pers
                self.images_person_now = self.images_person_with_tree_left
            elif self.which_way == 'right':
                self.x_coodr_person_osn += self.speed_pers
                self.images_person_now = self.images_person_with_tree_right
            else:
                self.images_person_now = self.images_person_with_tree_down  # стандарт

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

        self.x_coodr_person_osn, self.y_coodr_person_osn = self.x_coodr_person_osn, self.y_coodr_person_osn
        print(f'coord_person = {self.x_coodr_person_osn, self.y_coodr_person_osn}')

    def take_el(self, which_way):  # пробебел нажат
        self.which_way = which_way  # проверяем куда смотрит персонаж
        if self.which_way == 'up':
            self.images_person_now_take = self.images_person_take_throw_up[::-1]
        elif self.which_way == 'down':
            self.images_person_now_take = self.images_person_take_throw_down[::-1]
        elif self.which_way == 'left':
            self.images_person_now_take = self.images_person_take_throw_left[::-1]
        elif self.which_way == 'right':
            self.images_person_now_take = self.images_person_with_tree_right[::-1]
        self.take = 1
        self.index_take += 1
        self.in_the_hands = 1

        if self.index_take >= 9:
            self.index_take = 0
            self.take = 0

    def throw_el(self, which_way):
        self.which_way = which_way
        if self.which_way == 'up':
            self.images_person_now_throw = self.images_person_take_throw_up
        elif self.which_way == 'down':
            self.images_person_now_throw = self.images_person_take_throw_down
        elif self.which_way == 'left':
            self.images_person_now_throw = self.images_person_take_throw_left
        elif self.which_way == 'right':
            self.images_person_now_throw = self.images_person_with_tree_right
        self.throw = 1
        self.index_throw += 1
        self.in_the_hands = 0

        if self.index_take >= 9:
            self.index_throw = 0
            self.throw = 0

    def rendering(self):
        if self.take == 1:
            self.image_pers_take = pygame.transform.scale(self.images_person_now_take[self.index_take], (400, 400))
            screen.blit(self.image_pers_take, (self.x_coodr_person_osn, self.y_coodr_person_osn))
            Person.rendering.elll_in_the_hands = self.in_the_hands

        else:
            self.image_pers = pygame.transform.scale(self.images_person_now[self.index], (400, 400))
            screen.blit(self.image_pers, (self.x_coodr_person_osn, self.y_coodr_person_osn))
            Person.rendering.x_coodr_person_osn = self.x_coodr_person_osn
            Person.rendering.y_coodr_person_osn = self.y_coodr_person_osn
            Person.rendering.elll_in_the_hands = self.in_the_hands


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
