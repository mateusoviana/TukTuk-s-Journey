import pygame
from map_manager import MapManager
from player import Player
from config import TILE_SIZE
from ui import display_message_1

class Game:
    def __init__(self, window, clock):
        self.window = window
        self.clock = clock
        self.quit = False
        self.map_manager = MapManager()
        self.player = Player(self.window.get_height())
        self.message_shown = False

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

            print(self.player.x//TILE_SIZE, self.player.y//TILE_SIZE)
            # Verifica se o jogador está na posição da dica no mapa central
            if (self.map_manager.current_map_key == "centralMap" and 
                self.player.x // TILE_SIZE == 5 and 
                self.player.y // TILE_SIZE == 24 and 
                not self.message_shown):
                display_message_1("Cogumelos são a chave para encontrar sua irmã!", self.window)
                self.message_shown = True

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