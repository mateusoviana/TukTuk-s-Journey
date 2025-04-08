from pytmx.util_pygame import load_pygame
import pygame

class Map:
    def __init__(self, map_path):
        self.tmxdata = load_pygame(map_path)

    def draw(self, window, offset):
        for layer in self.tmxdata:
            for tile in layer.tiles():
                img = pygame.transform.scale(tile[2], (16,16))
                x = tile[0] * 16 + offset[0]
                y = tile[1] * 16 + offset[1]
                window.blit(img, (x, y))

    def get_tile_properties(self, x, y, offset):
        world_x = x - offset[0]
        world_y = y - offset[1]
        tile_x = world_x // 16
        tile_y = world_y // 16
        props = self.tmxdata.get_tile_properties(tile_x, tile_y, 0)
        return props if props else {"solid": 0}
