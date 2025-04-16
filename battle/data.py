CHARACTER_DATA = {
    'tuktuk': {
        'name': 'TukTuk',
        'stats': {
            'hp': 60,
            'attack': 55,
            'defense': 50,
            'speed': 60
        },
        'types': ['neutral'],
        'moves': [
            {'name': 'Fúria Lúcida', 'power': 40, 'type': 'normal', 'level_learned': 1},
            {'name': 'Rajada de Fumaça', 'power': 55, 'type': 'neutral', 'level_learned': 10},
            {'name': 'Baforada Venenosa', 'power': 60, 'type': 'neutral', 'level_learned': 15},
            {'name': 'TUK!', 'power': 70, 'type': 'wind', 'level_learned': 20}
        ],
        'sprites': {
            'back_default': 'battle/sprites/tuktukback.png'
        }
    },
    'water_boss': {
        'name': 'Water Boss',
        'stats': {
            'hp': 50,
            'attack': 45,
            'defense': 60,
            'speed': 40
        },
        'types': ['water'],
        'moves': [
            {'name': 'Splash', 'power': 40, 'type': 'water', 'level_learned': 1},
            {'name': "Jato dÁgua", 'power': 60, 'type': 'water', 'level_learned': 10},
            {'name': 'Rajada de Bolha', 'power': 45, 'type': 'water', 'level_learned': 15}
        ],
        'sprites': {
            'front_default': 'battle/sprites/waterboss.png',
        }
    },
    'fire_boss': {
        'name': 'Fire Boss',
        'stats': {
            'hp': 45,
            'attack': 65,
            'defense': 40,
            'speed': 55
        },
        'types': ['fire'],
        'moves': [
            {'name': 'Faísca Dinamite', 'power': 40, 'type': 'fire', 'level_learned': 1},
            {'name': 'Chicote Flamejante', 'power': 60, 'type': 'fire', 'level_learned': 12},
            {'name': 'Tornado de Fogo', 'power': 80, 'type': 'fire', 'level_learned': 18}
        ],
        'sprites': {
            'front_default': 'battle/sprites/fireboss.png'
        }
    },
    'earth_boss': {
        'name': 'Earth Boss',
        'stats': {
            'hp': 65,
            'attack': 50,
            'defense': 70,
            'speed': 35
        },
        'types': ['earth'],
        'moves': [
            {'name': 'Pedrada', 'power': 50, 'type': 'earth', 'level_learned': 1},
            {'name': 'Nuvem de Poeira', 'power': 55, 'type': 'earth', 'level_learned': 10},
            {'name': 'Terremoto', 'power': 75, 'type': 'earth', 'level_learned': 20}
        ],
        'sprites': {
            'front_default': 'battle/sprites/earthboss.png',
        }
    },
    'final_boss': {
        'name': 'Final Boss',
        'stats': {
            'hp': 50,
            'attack': 50,
            'defense': 45,
            'speed': 70
        },
        'types': ['neutral'],
        'moves': [
            {'name': 'Rajada', 'power': 40, 'type': 'neutral', 'level_learned': 1},
            {'name': 'Fúria de Tempestade', 'power': 60, 'type': 'neutral', 'level_learned': 12},
            {'name': 'Sopro da Morte', 'power': 80, 'type': 'neutral', 'level_learned': 20}
        ],
        'sprites': {
            'front_default': 'battle/sprites/windboss.png',
        }
    }
}
