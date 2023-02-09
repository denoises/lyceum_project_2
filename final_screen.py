import pygame
import os
import sys
import random
import sqlite3

pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
clock = pygame.time.Clock()


class Final:
    def __init__(self):
        con = sqlite3.connect('bd/BD_for_axmans.db')
        cursor = con.cursor()
        f = cursor.execute(f"""SELECT name, time FROM players_score""")

        self.bdrez = f.fetchall()
        print(str(self.bdrez))
        sp = []
        con.commit()
        con.close()

        self.my_font = pygame.font.SysFont(None, 30)

        self.y = 50
        self.x = 50
        for i in range(len(self.bdrez)):
            self.out = str(self.bdrez[i])
            text_surface = self.my_font.render(self.out, False, (255, 255, 255))
            screen.blit(text_surface, (self.x, self.y))
            self.y += 35

            self.rest = 'Перезапуск - R'
            text_surface_rest = self.my_font.render(self.rest, False, (255, 255, 255))
            screen.blit(text_surface_rest, (1650, 30))

            if self.y >= 900:
                self.x += 300
                self.y = 50


def main():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return

        screen.fill(pygame.Color((100, 100, 100)))
        Final()

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
