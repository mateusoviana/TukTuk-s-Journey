from map import Map
from config import TILE_SIZE

class MapManager:
    def __init__(self):
        self.maps = {
            "map1": Map("assets/EarthMap/earthMap.tmx"),
            "map2": Map("assets/Tileset1/map1.tmx"),
        }
        self.current_map_key = "map1"

        self.transition_points = {
            "map1": [
                {"condition": lambda p: p.x > 30*TILE_SIZE, "next": "map2", "new_x": 1*TILE_SIZE, "new_y": None}
            ],
            "map2": [
                {"condition": lambda p: p.x < TILE_SIZE, "next": "map1", "new_x": 30*TILE_SIZE, "new_y": 10*TILE_SIZE}
            ]
        }

    def get_current_map(self):
        return self.maps[self.current_map_key]

    def update_map_if_needed(self, player):
        for point in self.transition_points.get(self.current_map_key, []):
            if point["condition"](player):
                self._switch_map(point["next"], player, point)
                break  # evita múltiplas transições seguidas

    def _switch_map(self, new_map_key, player, point):
        self.current_map_key = new_map_key
        if point["new_x"] is not None:
            player.x = point["new_x"]
        if point["new_y"] is not None:
            player.y = point["new_y"]
        player.world_offset = [0, 0]  # reset offset da câmera

    def get_map_size(self):
        current = self.get_current_map()
        return current.tmxdata.width * TILE_SIZE, current.tmxdata.height * TILE_SIZE