from pytmx.util_pygame import load_pygame
import pygame
from config import TILE_SIZE
from map_data import MAPS


class Map:
    def __init__(self, map_name):
        map_data = MAPS.get(map_name)

        if map_data is None:
            raise ValueError(f"Map {map_name} not found!")

        self.map_path = map_data["map_path"]
        # self.music_path = map_data["music_path]

        self.tmxdata = load_pygame(self.map_path)

    def draw(self, window):
        for layer in self.tmxdata:
            for tile in layer.tiles():
                img = pygame.transform.scale(tile[2], (TILE_SIZE,TILE_SIZE))
                x = tile[0] * TILE_SIZE
                y = tile[1] * TILE_SIZE
                window.blit(img, (x, y))

    def get_tile_properties(self, x, y):
        world_x = x
        world_y = y
        tile_x = world_x // TILE_SIZE
        tile_y = world_y // TILE_SIZE

        width = self.tmxdata.width
        height = self.tmxdata.height
        if not (0 <= tile_x < width and 0 <= tile_y < height):
            return {"solid": 1, "water": 0, "grass": 0}

        properties = {"solid": 0, "water": 0, "grass": 0}
        
        for layer_index, layer in enumerate(self.tmxdata.visible_layers):
            props = self.tmxdata.get_tile_properties(tile_x, tile_y, layer_index)
            if props:
                if props.get("solid") == 1:
                    properties["solid"] = 1
                if props.get("water") == 1:
                    properties["water"] = 1
                if props.get("grass") == 1:
                    properties["grass"] = 1

        return properties

