import pygame
from pygame.sprite import Sprite


class Array2D:
    """
        Инструкция:
                         1. Методы строительства требуют двух параметров, а именно в широком и высоком двумерном массиве
                         2. Переменные участника W и H широко и высоки двумерного массива
                         3. Используйте: «Объект [X] [Y]» может принимать непосредственно к соответствующему значению
                         4. Значение по умолчанию массив 0
    """

    def __init__(self, w, h, default=0):
        self.w = w
        self.h = h
        self.data = []
        self.data = [[default for y in range(h)] for x in range(w)]

    def show_array2d(self):
        for y in range(self.h):
            for x in range(self.w):
                print(self.data[x][y], end=' ')
            print("")

    def __getitem__(self, item):
        return self.data[item]


class GameMap(Array2D):
    """
         Карта игры класс
    """

    def __init__(self, bottom, top, x, y):
        # Разделите карту в маленькую решетку W * H, каждая сетка 32 * 32 пикселей
        w = int(bottom.get_width() / 32) + 1
        h = int(top.get_height() / 32) + 1
        super().__init__(w, h)
        self.bottom = bottom
        self.top = top
        self.x = x
        self.y = y

    def draw_bottom(self, screen_surf):
        screen_surf.blit(self.bottom, (self.x, self.y))

    def draw_top(self, screen_surf):
        screen_surf.blit(self.top, (self.x, self.y))

    def load_walk_file(self, path):
        """
                 Прочитайте линию файла ходьбы
        """
        with open(path, 'r') as file:
            for x in range(self.w):
                for y in range(self.h):
                    v = int(file.readline())
                    self[x][y] = v
        self.show_array2d()

    def __init_game(self):
        self.hero = pygame.image.load('./img/character/hero.png').convert_alpha()
        self.map_bottom = pygame.image.load('./img/map/0.png').convert_alpha()
        self.map_top = pygame.image.load('./img/map/0_top.png').convert_alpha()
        self.game_map = GameMap(self.map_bottom, self.map_top, 0, 0)
        self.game_map.load_walk_file('./img/map/0.map')

    def update(self):
        window = pygame.display.set_mode((1920, 1080))
        clock = pygame.time.Clock()
        FPS = 60

        while True:
            self.clock.tick(self.FPS)
            self.event_handler()
            self.game_map.draw_bottom(self.screen_surf)
            Sprite.draw(self.screen_surf, self.hero, 100, 100, 0, 0)
            Sprite.draw(self.screen_surf, self.hero, 210, 120, 1, 1)
            Sprite.draw(self.screen_surf, self.hero, 300, 100, 2, 2)
            self.game_map.draw_top(self.screen_surf)
            pygame.display.update()
