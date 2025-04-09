import pygame

from config import TILE_SIZE

class Player:
    def __init__(self, window_height):
        self.x = 20*TILE_SIZE
        self.y_ground = window_height - TILE_SIZE
        self.y = 19*TILE_SIZE
        self.direction = "stand"
        self.world_offset = [0, 0]
        self.load_sprites()
        self.right_frame = 0
        self.left_frame = 0

    def load_sprites(self):
        self.stand = pygame.transform.scale(pygame.image.load("assets/p3/p3_stand.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
        self.jump = pygame.transform.scale(pygame.image.load("assets/p3/p3_jump.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
        self.duck = pygame.transform.scale(pygame.image.load("assets/p3/p3_duck.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))

        right_paths = [f"assets/p3/PNG/p3_walk{str(i).zfill(2)}.png" for i in range(1, 12)]
        self.right = [pygame.transform.scale(pygame.image.load(p).convert_alpha(), (TILE_SIZE, TILE_SIZE)) for p in right_paths]
        self.left = [pygame.transform.flip(img, True, False) for img in self.right]

    def handle_keys(self, keys, map_obj, window):
        move_map = {
            pygame.K_a: ("left", -1*TILE_SIZE, 0),
            pygame.K_d: ("right", TILE_SIZE, 0),
            pygame.K_w: ("up", 0, -1*TILE_SIZE),
            pygame.K_s: ("down", 0, TILE_SIZE),
        }
        moved = False
        
        current_tile = map_obj.get_tile_properties(self.x, self.y, self.world_offset)
        speed_multiplier = 1.0
        if current_tile["water"] == 1:
            speed_multiplier = 0.2
        if current_tile["grass"] == 1:
            speed_multiplier = 0.1
        
        for key, (dir, dx, dy) in move_map.items():
            if keys[key]:
                self.direction = dir
                new_x, new_y = self.x + dx, self.y + dy
                block = map_obj.get_tile_properties(new_x, new_y, self.world_offset)
                if block["solid"] == 0:
                    self.x += dx * speed_multiplier
                    self.y += dy * speed_multiplier
                moved = True
                break

        if not moved:
            self.direction = "stand"

    def update(self, map_obj, window):
        if self.x < 0: self.x = 0
        if self.x > window.get_width() - TILE_SIZE: self.x = window.get_width() - TILE_SIZE
        if self.y < 0: self.y = 0
        if self.y > window.get_height() - TILE_SIZE: self.y = window.get_height() - TILE_SIZE

    def draw(self, window):
        if self.direction == "stand":
            window.blit(self.stand, (self.x, self.y))
        elif self.direction == "up":
            window.blit(self.jump, (self.x, self.y))
        elif self.direction == "down":
            window.blit(self.duck, (self.x, self.y))
        elif self.direction == "right":
            window.blit(self.right[self.right_frame], (self.x, self.y))
            self.right_frame = (self.right_frame + 1) % len(self.right)
        elif self.direction == "left":
            window.blit(self.left[self.left_frame], (self.x, self.y))
            self.left_frame = (self.left_frame + 1) % len(self.left)