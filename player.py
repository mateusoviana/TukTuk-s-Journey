import pygame

<<<<<<< HEAD
class Player:
    def __init__(self, window_height):
        self.x = 480
        self.y_ground = window_height - 16
        self.y = self.y_ground - 160
=======
from config import TILE_SIZE


class Player:
    def __init__(self, window_height):
        self.x = 30*TILE_SIZE
        self.y_ground = window_height - TILE_SIZE
        self.y = 10*TILE_SIZE
>>>>>>> 6b8b3861090bd0cc7870a4b8408fb2139d08577a
        self.direction = "stand"
        self.world_offset = [0, 0]
        self.load_sprites()
        self.right_frame = 0
        self.left_frame = 0

    def load_sprites(self):
<<<<<<< HEAD
        self.stand = pygame.transform.scale(pygame.image.load("assets/p3/p3_stand.png").convert_alpha(), (16,16))
        self.jump = pygame.transform.scale(pygame.image.load("assets/p3/p3_jump.png").convert_alpha(), (16,16))
        self.duck = pygame.transform.scale(pygame.image.load("assets/p3/p3_duck.png").convert_alpha(), (16,16))

        right_paths = [f"assets/p3/PNG/p3_walk{str(i).zfill(2)}.png" for i in range(1,12)]
        self.right = [pygame.transform.scale(pygame.image.load(p).convert_alpha(), (16,16)) for p in right_paths]
=======
        self.stand = pygame.transform.scale(pygame.image.load("assets/p3/p3_stand.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
        self.jump = pygame.transform.scale(pygame.image.load("assets/p3/p3_jump.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
        self.duck = pygame.transform.scale(pygame.image.load("assets/p3/p3_duck.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))

        right_paths = [f"assets/p3/PNG/p3_walk{str(i).zfill(2)}.png" for i in range(1, 12)]
        self.right = [pygame.transform.scale(pygame.image.load(p).convert_alpha(), (TILE_SIZE, TILE_SIZE)) for p in right_paths]
>>>>>>> 6b8b3861090bd0cc7870a4b8408fb2139d08577a
        self.left = [pygame.transform.flip(img, True, False) for img in self.right]

    def handle_keys(self, keys, map_obj, window):
        move_map = {
<<<<<<< HEAD
            pygame.K_a: ("left", -16, 0),
            pygame.K_d: ("right", 16, 0),
            pygame.K_w: ("up", 0, -16),
            pygame.K_s: ("down", 0, 16),
=======
            pygame.K_a: ("left", -1*TILE_SIZE, 0),
            pygame.K_d: ("right", TILE_SIZE, 0),
            pygame.K_w: ("up", 0, -1*TILE_SIZE),
            pygame.K_s: ("down", 0, TILE_SIZE),
>>>>>>> 6b8b3861090bd0cc7870a4b8408fb2139d08577a
        }
        moved = False
        for key, (dir, dx, dy) in move_map.items():
            if keys[key]:
                self.direction = dir
                new_x, new_y = self.x + dx, self.y + dy
<<<<<<< HEAD
                if 0 <= new_x <= window.get_width() - 16 and 0 <= new_y <= window.get_height() - 16:
                    block = map_obj.get_tile_properties(new_x, new_y, self.world_offset)
                    if block["solid"] == 0:
                        self.x += dx
                        self.y += dy
=======
                block = map_obj.get_tile_properties(new_x, new_y, self.world_offset)
                if block["solid"] == 0:
                    self.x += dx
                    self.y += dy
>>>>>>> 6b8b3861090bd0cc7870a4b8408fb2139d08577a
                moved = True
                break

        if not moved:
            self.direction = "stand"

    def update(self, map_obj, window):
<<<<<<< HEAD
        # Manter limites ou lógica extra se quiser
        if self.x < 0: self.x = 0
        if self.x > window.get_width() - 16: self.x = window.get_width() - 16
=======
        if self.x < 0: self.x = 0
        if self.x > window.get_width() - TILE_SIZE: self.x = window.get_width() - TILE_SIZE
>>>>>>> 6b8b3861090bd0cc7870a4b8408fb2139d08577a
        if self.y < 0: self.y = 0
        if self.y > self.y_ground: self.y = self.y_ground

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
<<<<<<< HEAD
            self.left_frame = (self.left_frame + 1) % len(self.left)
=======
            self.left_frame = (self.left_frame + 1) % len(self.left)
>>>>>>> 6b8b3861090bd0cc7870a4b8408fb2139d08577a
