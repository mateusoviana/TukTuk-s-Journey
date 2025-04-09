class Move:
    def __init__(self, move_data):
        self.name = move_data['name']
        self.power = move_data['power']
        self.type = move_data['type']
        