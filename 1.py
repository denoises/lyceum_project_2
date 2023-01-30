import pygame
import os


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size



    def render(self, screen):
        # ground = load_image('image/low_settings/ground/ground0001.png')
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, 'green',
                (x * self.cell_size + self.left,
                 y * self.cell_size + self.top,
                 self.cell_size, self.cell_size), 1)


def main():
    board = Board(100, 100)  # КОЛЛИЧЕСТВО КЕЛТОК
    board.set_view(0, 0, 100)
    running = True
    pygame.init()
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            screen.fill('#000000')
            board.render(screen)
            pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
