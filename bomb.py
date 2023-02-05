import pygame
import sys
import os
import random

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()


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

class Bomb(pygame.sprite.Sprite):
    image = load_image("img/bomb.png")
    image_boom = load_image("img/boom.png")
    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        while True:
            self.rect.x = random.randrange(10, 800)
            self.rect.y = random.randrange(10, 800)
            if self.rect.collidepoint(self, all_sprites):
                break

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and\
            self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom





def main():
    running = True
    start = True

    x = 0
    f = True

    cursor = pygame.sprite.Sprite()
    for i in range(50):
        Bomb(all_sprites)


    pygame.mouse.set_visible(False)
    while running:
        if x + 200  > 500:
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
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_SPACE):
                start = not start
            all_sprites.update(event)
        screen.fill('#000000')
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
