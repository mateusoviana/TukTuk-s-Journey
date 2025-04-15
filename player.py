import pygame

from config import TILE_SIZE

class Player:
    def __init__(self, window_height):
        self.x = 20*TILE_SIZE
        self.y_ground = window_height - TILE_SIZE
        self.y = 19*TILE_SIZE
        self.direction = "down"
        self.world_offset = [0, 0]
        self.load_sprites()
        self.up_frame = 0
        self.down_frame = 0
        self.right_frame = 0
        self.left_frame = 0

    def load_sprites(self):
        self.front = pygame.transform.scale(pygame.image.load("assets/p3/f1.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
        self.back = pygame.transform.scale(pygame.image.load("assets/p3/b1.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
        self.right = pygame.transform.scale(pygame.image.load("assets/p3/r1.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
        self.left = pygame.transform.scale(pygame.image.load("assets/p3/l1.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))

        up_paths = [f"assets/p3/b{str(i)}.png" for i in range(1, 4)]
        self.up_walk = [pygame.transform.scale(pygame.image.load(p).convert_alpha(), (TILE_SIZE, TILE_SIZE)) for p in up_paths]

        down_paths = [f"assets/p3/f{str(i)}.png" for i in range(1, 4)]
        self.down_walk = [pygame.transform.scale(pygame.image.load(p).convert_alpha(), (TILE_SIZE, TILE_SIZE)) for p in down_paths]

        right_paths = [f"assets/p3/r{str(i)}.png" for i in range(1, 5)]
        self.right_walk = [pygame.transform.scale(pygame.image.load(p).convert_alpha(), (TILE_SIZE, TILE_SIZE)) for p in right_paths]
        self.left_walk = [pygame.transform.flip(img, True, False) for img in self.right_walk]

    def handle_keys(self, keys, map_obj, window):
        move_map = {
            pygame.K_a: ("left_walk", -1*TILE_SIZE, 0),
            pygame.K_d: ("right_walk", TILE_SIZE, 0),
            pygame.K_w: ("up_walk", 0, -1*TILE_SIZE),
            pygame.K_s: ("down_walk", 0, TILE_SIZE),
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
            if self.direction == "left_walk":
                self.direction = "left"
            if self.direction == "right_walk":
                self.direction = "right"
            if self.direction == "down_walk":
                self.direction = "down"
            if self.direction == "up_walk":
                self.direction = "up"

    def update(self, map_obj, window):
        if self.x < 0: self.x = 0
        if self.x > window.get_width() - TILE_SIZE: self.x = window.get_width() - TILE_SIZE
        if self.y < 0: self.y = 0
        if self.y > window.get_height() - TILE_SIZE: self.y = window.get_height() - TILE_SIZE

    def draw(self, window):
        if self.direction == "down":
            window.blit(self.front, (self.x, self.y))
        elif self.direction == "up":
            window.blit(self.back, (self.x, self.y))
        elif self.direction == "right":
            window.blit(self.right, (self.x, self.y))
        elif self.direction == "left":
            window.blit(self.left, (self.x, self.y))
        elif self.direction == "up_walk":
            window.blit(self.up_walk[self.up_frame], (self.x, self.y))
            self.up_frame = (self.up_frame + 1) % len(self.up_walk)
        elif self.direction == "down_walk":
            window.blit(self.down_walk[self.down_frame], (self.x, self.y))
            self.down_frame = (self.down_frame + 1) % len(self.down_walk)
        elif self.direction == "right_walk":
            window.blit(self.right_walk[self.right_frame], (self.x, self.y))
            self.right_frame = (self.right_frame + 1) % len(self.right_walk)
        elif self.direction == "left_walk":
            window.blit(self.left_walk[self.left_frame], (self.x, self.y))
            self.left_frame = (self.left_frame + 1) % len(self.left_walk)