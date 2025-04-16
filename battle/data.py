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
            {'name': 'dash strike', 'power': 40, 'type': 'normal', 'level_learned': 1},
            {'name': 'spin kick', 'power': 55, 'type': 'neutral', 'level_learned': 10},
            {'name': 'focus power', 'power': 0, 'type': 'neutral', 'level_learned': 15},
            {'name': 'tornado burst', 'power': 70, 'type': 'wind', 'level_learned': 20}
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
            {'name': 'water splash', 'power': 40, 'type': 'water', 'level_learned': 1},
            {'name': 'aqua jet', 'power': 60, 'type': 'water', 'level_learned': 10},
            {'name': 'bubble burst', 'power': 45, 'type': 'water', 'level_learned': 15}
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
            {'name': 'ember blast', 'power': 40, 'type': 'fire', 'level_learned': 1},
            {'name': 'flame whip', 'power': 60, 'type': 'fire', 'level_learned': 12},
            {'name': 'burning rage', 'power': 80, 'type': 'fire', 'level_learned': 18}
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
            {'name': 'rock throw', 'power': 50, 'type': 'earth', 'level_learned': 1},
            {'name': 'mud shot', 'power': 55, 'type': 'earth', 'level_learned': 10},
            {'name': 'stone crush', 'power': 75, 'type': 'earth', 'level_learned': 20}
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
            {'name': 'gust', 'power': 40, 'type': 'neutral', 'level_learned': 1},
            {'name': 'air slice', 'power': 60, 'type': 'neutral', 'level_learned': 12},
            {'name': 'tempest fury', 'power': 80, 'type': 'neutral', 'level_learned': 20}
        ],
        'sprites': {
            'front_default': 'battle/sprites/windboss.png',
        }
    }
}
