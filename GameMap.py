import pygame


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

GameMap()