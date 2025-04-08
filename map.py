from pytmx.util_pygame import load_pygame
import pygame
from config import TILE_SIZE


class Map:
    def __init__(self, map_path):
        self.tmxdata = load_pygame(map_path)

    def draw(self, window, offset):
        for layer in self.tmxdata:
            for tile in layer.tiles():
                img = pygame.transform.scale(tile[2], (TILE_SIZE,TILE_SIZE))
                x = tile[0] * TILE_SIZE + offset[0]
                y = tile[1] * TILE_SIZE + offset[1]
                window.blit(img, (x, y))

    def get_tile_properties(self, x, y, offset):
        world_x = x - offset[0]
        world_y = y - offset[1]
        tile_x = world_x // TILE_SIZE
        tile_y = world_y // TILE_SIZE

        width = self.tmxdata.width
        height = self.tmxdata.height
        if not (0 <= tile_x < width and 0 <= tile_y < height):
            return {"solid": 1}

        for layer_index, layer in enumerate(self.tmxdata.visible_layers):
            props = self.tmxdata.get_tile_properties(tile_x, tile_y, layer_index)
            if props and props.get("solid") == 1:
                return {"solid": 1}

        return {"solid": 0}

