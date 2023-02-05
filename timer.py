import pygame
import pygame.freetype
import sys

which_way = 'up'

pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
clock = pygame.time.Clock()


class Timer:
    def __init__(self):
        self.font = pygame.freetype.SysFont(None, 20)
        self.font.origin = True
        ticks = pygame.time.get_ticks()
        millis = ticks % 1000
        seconds = int(ticks / 1000 % 60)
        minutes = int(ticks / 60000 % 24)
        self.out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
        self.font.render_to(screen, (932, 30), self.out, pygame.Color((255, 255, 255)))


def main():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: return

        screen.fill(pygame.Color((100, 100, 100)))
        Timer()

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__': main()
