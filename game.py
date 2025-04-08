import pygame
from map import Map
from player import Player

class Game:
    def __init__(self, window, clock):
        self.window = window
        self.clock = clock
        self.quit = False
        self.map = Map("assets/EarthTiles/sampleMap.tmx")
        self.player = Player(self.window.get_height())

    def run(self):
        while not self.quit:
            self.window.fill((64,64,64))
            self.map.draw(self.window, self.player.world_offset)
            self.handle_events()
            self.player.update(self.map, self.window)
            self.player.draw(self.window)
            pygame.display.update()
            self.clock.tick(15)

    def handle_events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
        self.player.handle_keys(keys, self.map, self.window)
