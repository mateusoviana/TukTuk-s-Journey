from config import TILE_SIZE
from map_data import MAPS, MAP_PATHS, TRANSITION_POINTS, CURRENT_MAP_KEY, MESSAGE_POINTS, BATTLE_POINTS, EXTRA_POINTS

class MapManager:
    def __init__(self):
        self.map_paths = MAP_PATHS
        self.current_map_key = CURRENT_MAP_KEY

        self.transition_points = TRANSITION_POINTS
        self.message_points = MESSAGE_POINTS


        self.battle_points = BATTLE_POINTS
        self.extra_points = EXTRA_POINTS

    def get_current_map(self):
        return MAPS.get_map(self.current_map_key, self.map_paths[self.current_map_key])


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

    def check_battle_point(self, player_x, player_y):
        """Verifica se o jogador está em um ponto de batalha e retorna o inimigo se estiver"""
        battle_points = self.battle_points.get(self.current_map_key, [])
        for point in battle_points:
            if player_x == point["x"] and player_y == point["y"]:
                return point["enemy"]
        return None
    
    def get_extra_points(self, player_x, player_y):
        extra_points = self.extra_points.get(self.current_map_key, [])
        for point in extra_points:
            if player_x == point["x"] and player_y == point["y"]:
                return point["extra"]
        return None