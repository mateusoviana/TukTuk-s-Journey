from map import Map
from config import TILE_SIZE

class MapManager:
    def __init__(self):
        self.maps = {
            "centralMap": Map("assets/HomeMap/HomeMap.tmx"),
            "earthMap": Map("assets/EarthMap/earthMap.tmx"),
            "waterMap": Map("assets/WaterMap/waterMap.tmx"),
            "fireMap": Map("assets/FireMap/fireMap.tmx"),
        }
        self.current_map_key = "centralMap"

        self.transition_points = {
            "centralMap": [
                {"condition": lambda p: p.x < TILE_SIZE and p.y > TILE_SIZE*13 and p.y < TILE_SIZE*15, "next": "earthMap", "new_x": 30*TILE_SIZE, "new_y": 10*TILE_SIZE},
                {"condition": lambda p: p.x > 13*TILE_SIZE and p.x < 15*TILE_SIZE and p.y > 28 * TILE_SIZE, "next": "waterMap", "new_x": 9*TILE_SIZE, "new_y": 1 * TILE_SIZE},
                {"condition": lambda p: p.x > 28*TILE_SIZE and p.y > 12*TILE_SIZE and p.y < 14 * TILE_SIZE, "next": "fireMap", "new_x": TILE_SIZE, "new_y": 10 * TILE_SIZE},
            ],
            "earthMap": [
                {"condition": lambda p: p.x > 30 * TILE_SIZE, "next": "centralMap", "new_x": 1 * TILE_SIZE,
                 "new_y": 14 * TILE_SIZE}
            ],
            "waterMap": [
                {"condition": lambda p: p.y < 1 * TILE_SIZE, "next": "centralMap", "new_x": 14 * TILE_SIZE, "new_y": 28 * TILE_SIZE,}
            ],
            "fireMap": [
                {"condition": lambda p: p.x < TILE_SIZE and p.y > 8*TILE_SIZE and p.y < 10 * TILE_SIZE, "next": "centralMap", "new_x": 28 * TILE_SIZE, "new_y": 13 * TILE_SIZE},
            ]
        }

    def get_current_map(self):
        return self.maps[self.current_map_key]

    def update_map_if_needed(self, player):
        for point in self.transition_points.get(self.current_map_key, []):
            if point["condition"](player):
                self._switch_map(point["next"], player, point)
                break

    def _switch_map(self, new_map_key, player, point):
        self.current_map_key = new_map_key
        if point["new_x"] is not None:
            player.x = point["new_x"]
        if point["new_y"] is not None:
            player.y = point["new_y"]
        player.world_offset = [0, 0]

    def get_map_size(self):
        current = self.get_current_map()
        return current.tmxdata.width * TILE_SIZE, current.tmxdata.height * TILE_SIZE