import pygame
from map_manager import MapManager
from player import Player
from config import TILE_SIZE
from ui import display_message_points

class Game:
    def __init__(self, window, clock):
        self.window = window
        self.clock = clock
        self.quit = False
        self.map_manager = MapManager()
        self.player = Player(self.window.get_height())
        self.last_message_pos = None

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

            # Verificação de mensagens:

            player_tile_x = self.player.x // TILE_SIZE
            player_tile_y = self.player.y // TILE_SIZE
            current_pos = (player_tile_x, player_tile_y)
            print(current_pos)
            
            message_points_for_map = self.map_manager.message_points.get(self.map_manager.current_map_key, [])
            message_to_display = None
            point_found = None

            for point in message_points_for_map:
                if player_tile_x == point["x"] and player_tile_y == point["y"]:
                    message_to_display = point["message"]
                    point_found = (point["x"], point["y"])
                    break
            
            if message_to_display and current_pos != self.last_message_pos:
                display_message_points(message_to_display, self.window)
                self.last_message_pos = current_pos
            elif not message_to_display:
                self.last_message_pos = None

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