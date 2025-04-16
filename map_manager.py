from map import Map
from map_data import MAPS, TRANSITION_POINTS, MESSAGE_POINTS, BATTLE_POINTS, EXTRA_POINTS
from config import TILE_SIZE
from battle.character import Hero, Enemy
from battle.data import CHARACTER_DATA
from ui import display_message_points

class MapManager:
    def __init__(self):
        self.maps = {
            map_name: Map(map_name)
            for map_name in MAPS
        }
        self.current_map_key = "centralMap"
        self.game = None  # Referência ao jogo será definida posteriormente
        self.transition_points = TRANSITION_POINTS
        self.message_points = MESSAGE_POINTS
        self.battle_points = BATTLE_POINTS
        self.extra_points = EXTRA_POINTS


    def get_current_map(self):
        return self.maps[self.current_map_key]

    def update_map_if_needed(self, player):
        for point in self.transition_points.get(self.current_map_key, []):
            if point["condition"](player):
                self._switch_map(point["next"], player, point)
                break

    def _switch_map(self, new_map_key, player, point):
        # Verifica se é uma tentativa de acessar o bossMap
        if new_map_key == "bossMap" and not self.game.can_access_boss_map():
            # Exibe mensagem informando que precisa derrotar todos os bosses
            display_message_points("Você precisa derrotar todos os bosses antes de acessar esta área!", self.game.window)
            return  # Não permite a transição
        
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

    def set_game(self, game):
        self.game = game

