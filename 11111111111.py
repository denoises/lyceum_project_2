import pygame
import sys
import os
import random

pygame.init()
size = width, height = 820, 820
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()


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

class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)

    def update(self, *args):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)



def main():
    running = True
    start = True
    clock = pygame.time.Clock()
    Border(5, 5, 815, 5)
    Border(5, 815, 815, 815)
    Border(5, 5, 5, 815)
    Border(815, 5, 815, 815)

    for i in range(20):
        Ball(20, 100, 100)

    x = 0
    f = True
    cursor = pygame.sprite.Sprite()
    while running:
        if x + 200 > 500:
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
