from map import Map
from battle.character import Enemy
from battle.data import CHARACTER_DATA
from config import TILE_SIZE

class MapContainer:
    def __init__(self):
        self.maps = {}

    def get_map(self, key, map_path):
        if key not in self.maps:
            self.maps[key] = Map(map_path)
        return self.maps[key]


MAPS = MapContainer()

CURRENT_MAP_KEY = "centralMap"

MAP_PATHS = {
    "centralMap": "assets/HomeMap/HomeMap.tmx",
    "earthMap": "assets/EarthMap/earthMap.tmx",
    "waterMap": "assets/WaterMap/waterMap.tmx",
    "fireMap": "assets/FireMap/fireMap.tmx",
    "bossMap": "assets/FireMap/fireMap.tmx",
}

TRANSITION_POINTS = {
    "centralMap": [
        {
            "condition": lambda p: p.x < TILE_SIZE and TILE_SIZE * 13 < p.y < TILE_SIZE * 15,
            "next": "earthMap",
            "new_x": 30 * TILE_SIZE,
            "new_y": 10 * TILE_SIZE,
        },
        {
            "condition": lambda p: 13 * TILE_SIZE < p.x < 15 * TILE_SIZE and p.y > 28 * TILE_SIZE,
            "next": "waterMap",
            "new_x": 9 * TILE_SIZE,
            "new_y": 1 * TILE_SIZE,
        },
        {
            "condition": lambda p: p.x > 28 * TILE_SIZE and 12 * TILE_SIZE < p.y < 14 * TILE_SIZE,
            "next": "fireMap",
            "new_x": TILE_SIZE,
            "new_y": 10 * TILE_SIZE,
        },
        {
            "condition": lambda p: 13 * TILE_SIZE < p.x < 16 * TILE_SIZE and p.y < 4 * TILE_SIZE,
            "next": "bossMap",
            "new_x": 28 * TILE_SIZE,
            "new_y": 13 * TILE_SIZE,
        },
    ],
    "earthMap": [
        {
            "condition": lambda p: p.x > 30 * TILE_SIZE,
            "next": "centralMap",
            "new_x": 1 * TILE_SIZE,
            "new_y": 14 * TILE_SIZE,
        },
    ],
    "waterMap": [
        {
            "condition": lambda p: p.y < 1 * TILE_SIZE,
            "next": "centralMap",
            "new_x": 14 * TILE_SIZE,
            "new_y": 28 * TILE_SIZE,
        },
    ],
    "fireMap": [
        {
            "condition": lambda p: p.x < TILE_SIZE and 8 * TILE_SIZE < p.y < 10 * TILE_SIZE,
            "next": "centralMap",
            "new_x": 28 * TILE_SIZE,
            "new_y": 13 * TILE_SIZE,
        },
    ],
    "bossMap": [
        {
            "condition": lambda p: 13 * TILE_SIZE < p.x < 16 * TILE_SIZE and p.y < 4 * TILE_SIZE,
            "next": "centralMap",
            "new_x": 28 * TILE_SIZE,
            "new_y": 13 * TILE_SIZE,
        },
    ]
}

MESSAGE_POINTS = {
    "centralMap": [
        {"x": 5, "y": 24, "message": "Cogumelos são a chave para encontrar sua irmã!"},
        {"x": 24, "y": 8, "message": "NÃO TENHO NADA PARA TE DAR!"},
        {"x": 23, "y": 26, "message": "Desculpe, não posso te ajudar!"},
        {"x": 14, "y": 22, "message": "Procure em outro lugar!"},
        {"x": 6, "y": 13, "message": "Z...Z...Z...!"},
        {"x": 9, "y": 3, "message": "SAIA DAQUI!"},
    ],
    "fireMap": [
        {"x": 2, "y": 4, "message": "Eita quintura do diabo!"},
    ],
    "earthMap": [
        {"x": 11, "y": 2, "message": "Está fechado!"},
    ],
    "waterMap": [
        {"x": 6, "y": 2, "message": "Tente não se afogar!"},
    ],
}

BATTLE_POINTS = {
    "centralMap": [
        {
            "x": 15,
            "y": 15,
            "enemy": Enemy("Wind Boss", CHARACTER_DATA["wind_boss"], level=25, x=0, y=0),
        },
    ],
    "fireMap": [
        {
            "x": 26,
            "y": 11,
            "enemy": Enemy("Fire Boss", CHARACTER_DATA["fire_boss"], level=25, x=0, y=0),
        },
    ],
    "waterMap": [
        {
            "x": 9,
            "y": 29,
            "enemy": Enemy("Water Boss", CHARACTER_DATA["water_boss"], level=25, x=0, y=0),
        },
    ],
    "earthMap": [
        {
            "x": 3,
            "y": 10,
            "enemy": Enemy("Earth Boss", CHARACTER_DATA["earth_boss"], level=25, x=0, y=0),
        },
    ],
}

EXTRA_POINTS = {
    "earthMap": [
        {"x": 20, "y": 16, "extra": "potion"},
    ],
}
