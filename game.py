import pygame
<<<<<<< HEAD
from map import Map
from player import Player
=======
from map_manager import MapManager
from player import Player
from config import TILE_SIZE
>>>>>>> 6b8b3861090bd0cc7870a4b8408fb2139d08577a

class Game:
    def __init__(self, window, clock):
        self.window = window
        self.clock = clock
        self.quit = False
<<<<<<< HEAD
        self.map = Map("assets/EarthTiles/sampleMap.tmx")
=======
        self.map_manager = MapManager()
>>>>>>> 6b8b3861090bd0cc7870a4b8408fb2139d08577a
        self.player = Player(self.window.get_height())

    def run(self):
        while not self.quit:
<<<<<<< HEAD
            self.window.fill((64,64,64))
            self.map.draw(self.window, self.player.world_offset)
            self.handle_events()
            self.player.update(self.map, self.window)
            self.player.draw(self.window)
=======
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

            # Checa se precisa trocar de mapa (e reposicionar o player)
            self.map_manager.update_map_if_needed(self.player)

>>>>>>> 6b8b3861090bd0cc7870a4b8408fb2139d08577a
            pygame.display.update()
            self.clock.tick(15)

    def handle_events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
<<<<<<< HEAD
        self.player.handle_keys(keys, self.map, self.window)
=======

        # Usa o mapa atual do MapManager
        current_map = self.map_manager.get_current_map()
        self.player.handle_keys(keys, current_map, self.window)
>>>>>>> 6b8b3861090bd0cc7870a4b8408fb2139d08577a
