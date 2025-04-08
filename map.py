from pytmx.util_pygame import load_pygame
import pygame
<<<<<<< HEAD
=======
from config import TILE_SIZE

>>>>>>> 6b8b3861090bd0cc7870a4b8408fb2139d08577a

class Map:
    def __init__(self, map_path):
        self.tmxdata = load_pygame(map_path)

    def draw(self, window, offset):
        for layer in self.tmxdata:
            for tile in layer.tiles():
<<<<<<< HEAD
                img = pygame.transform.scale(tile[2], (16,16))
                x = tile[0] * 16 + offset[0]
                y = tile[1] * 16 + offset[1]
=======
                img = pygame.transform.scale(tile[2], (TILE_SIZE,TILE_SIZE))
                x = tile[0] * TILE_SIZE + offset[0]
                y = tile[1] * TILE_SIZE + offset[1]
>>>>>>> 6b8b3861090bd0cc7870a4b8408fb2139d08577a
                window.blit(img, (x, y))

    def get_tile_properties(self, x, y, offset):
        world_x = x - offset[0]
        world_y = y - offset[1]
<<<<<<< HEAD
        tile_x = world_x // 16
        tile_y = world_y // 16
        props = self.tmxdata.get_tile_properties(tile_x, tile_y, 0)
        return props if props else {"solid": 0}
=======
        tile_x = world_x // TILE_SIZE
        tile_y = world_y // TILE_SIZE

        # Verificação de limites do mapa
        width = self.tmxdata.width
        height = self.tmxdata.height
        if 0 <= tile_x < width and 0 <= tile_y < height:
            props = self.tmxdata.get_tile_properties(tile_x, tile_y, 0)
            return props if props else {"solid": 0}
        else:
            return {"solid": 1}  # fora do mapa = bloqueado
>>>>>>> 6b8b3861090bd0cc7870a4b8408fb2139d08577a
