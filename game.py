import pygame
from map_manager import MapManager
from player import Player
from config import TILE_SIZE

class Game:
    def __init__(self, window, clock):
        self.window = window
        self.clock = clock
        self.quit = False
        self.map_manager = MapManager()
        self.player = Player(self.window.get_height())

    def run(self):
        while not self.quit:
            self.handle_events()

            current_map = self.map_manager.get_current_map()

            map_width = current_map.tmxdata.width * TILE_SIZE
            map_height = current_map.tmxdata.height * TILE_SIZE
            if (map_width, map_height) != self.window.get_size():
                self.window = pygame.display.set_mode((map_width, map_height))

            self.window.fill((64, 64, 64))
            current_map.draw(self.window, self.player.world_offset)

            self.player.update(current_map, self.window)
            self.player.draw(self.window)

            self.map_manager.update_map_if_needed(self.player)

            pygame.display.update()
            self.clock.tick(15)

    def handle_events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True

        current_map = self.map_manager.get_current_map()
        self.player.handle_keys(keys, current_map, self.window)