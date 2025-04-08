import pygame

class Player:
    def __init__(self, window_height):
        self.x = 480
        self.y_ground = window_height - 16
        self.y = self.y_ground - 160
        self.direction = "stand"
        self.world_offset = [0, 0]
        self.load_sprites()
        self.right_frame = 0
        self.left_frame = 0

    def load_sprites(self):
        self.stand = pygame.transform.scale(pygame.image.load("assets/p3/p3_stand.png").convert_alpha(), (16,16))
        self.jump = pygame.transform.scale(pygame.image.load("assets/p3/p3_jump.png").convert_alpha(), (16,16))
        self.duck = pygame.transform.scale(pygame.image.load("assets/p3/p3_duck.png").convert_alpha(), (16,16))

        right_paths = [f"assets/p3/PNG/p3_walk{str(i).zfill(2)}.png" for i in range(1,12)]
        self.right = [pygame.transform.scale(pygame.image.load(p).convert_alpha(), (16,16)) for p in right_paths]
        self.left = [pygame.transform.flip(img, True, False) for img in self.right]

    def handle_keys(self, keys, map_obj, window):
        move_map = {
            pygame.K_a: ("left", -16, 0),
            pygame.K_d: ("right", 16, 0),
            pygame.K_w: ("up", 0, -16),
            pygame.K_s: ("down", 0, 16),
        }
        moved = False
        for key, (dir, dx, dy) in move_map.items():
            if keys[key]:
                self.direction = dir
                new_x, new_y = self.x + dx, self.y + dy
                if 0 <= new_x <= window.get_width() - 16 and 0 <= new_y <= window.get_height() - 16:
                    block = map_obj.get_tile_properties(new_x, new_y, self.world_offset)
                    if block["solid"] == 0:
                        self.x += dx
                        self.y += dy
                moved = True
                break

        if not moved:
            self.direction = "stand"

    def update(self, map_obj, window):
        # Manter limites ou lógica extra se quiser
        if self.x < 0: self.x = 0
        if self.x > window.get_width() - 16: self.x = window.get_width() - 16
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
            self.left_frame = (self.left_frame + 1) % len(self.left)
