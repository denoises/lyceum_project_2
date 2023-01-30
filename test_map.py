import pygame
from pygame.sprite import Sprite

from GameMap import GameMap


class Main():
    def __init_game(self):
        self.hero = pygame.image.load('./img/character/hero.png').convert_alpha()
        self.map_bottom = pygame.image.load('./img/map/0.png').convert_alpha()
        self.map_top = pygame.image.load('./img/map/0_top.png').convert_alpha()
        self.game_map = GameMap(self.map_bottom, self.map_top, 0, 0)
        self.game_map.load_walk_file('./img/map/0.map')

    def update(self):
        while True:
            self.clock.tick(self.fps)

            self.event_handler()

            self.game_map.draw_bottom(self.screen_surf)
            Sprite.draw(self.screen_surf, self.hero, 100, 100, 0, 0)
            Sprite.draw(self.screen_surf, self.hero, 210, 120, 1, 1)
            Sprite.draw(self.screen_surf, self.hero, 300, 100, 2, 2)
            self.game_map.draw_top(self.screen_surf)
            pygame.display.update()