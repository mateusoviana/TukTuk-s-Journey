import pygame
import random
import time
import math
from move import Move

class Character(pygame.sprite.Sprite):
    def __init__(self, name, data, level, x, y):
        super().__init__()
        self.name = name
        self.level = level
        self.x, self.y = x, y
        self.num_potions = 3

        self.stats = data['stats']
        self.current_hp = self.stats['hp'] + level
        self.max_hp = self.current_hp
        self.attack = self.stats['attack']
        self.defense = self.stats['defense']
        self.speed = self.stats['speed']
        self.types = data['types']
        self.moves = [Move(m) for m in data['moves'] if m['power'] > 0 and level >= m['level_learned']]

        if len(self.moves) > 4:
            self.moves = random.sample(self.moves, 4)

        self.size = 150
        self.sprites = data['sprites']
        self.set_sprite('front_default')

    def set_sprite(self, side):
        path = self.sprites.get(side, None)
        if path:
            try:
                self.image = pygame.image.load(path).convert_alpha()
            except:
                self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
                pygame.draw.rect(self.image, (200, 200, 200), (0, 0, self.size, self.size))
        else:
            self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)

        scale = self.size / self.image.get_width()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))

    def perform_attack(self, target, move, game):
        from ui import display_message
        display_message(f'{self.name} usou {move.name}!', game)
        time.sleep(2)
        damage = (2 * self.level + 10) / 250 * self.attack / target.defense * move.power
        if move.type in self.types:
            damage *= 1.5
        if random.randint(1, 10000) <= 625:
            damage *= 1.5
        target.take_damage(int(damage))

    def take_damage(self, amount):
        self.current_hp = max(0, self.current_hp - amount)

    def use_potion(self):
        if self.num_potions > 0:
            self.current_hp = min(self.max_hp, self.current_hp + 30)
            self.num_potions -= 1

    def draw(self, game, alpha=255):
        sprite = self.image.copy()
        transparency = (255, 255, 255, alpha)
        sprite.fill(transparency, None, pygame.BLEND_RGBA_MULT)
        game.blit(sprite, (self.x, self.y))

    def draw_hp(self, game):
        red = (200, 0, 0)
        green = (0, 200, 0)
        black = (0, 0, 0)
        bar_scale = 200 // self.max_hp
        for i in range(self.max_hp):
            bar = (self.hp_x + bar_scale * i, self.hp_y, bar_scale, 20)
            pygame.draw.rect(game, red, bar)

        for i in range(self.current_hp):
            bar = (self.hp_x + bar_scale * i, self.hp_y, bar_scale, 20)
            pygame.draw.rect(game, green, bar)

        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render(f'HP: {self.current_hp} / {self.max_hp}', True, black)
        text_rect = text.get_rect()
        text_rect.x = self.hp_x
        text_rect.y = self.hp_y + 30
        game.blit(text, text_rect)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())


class Hero(Character):
    pass


class Enemy(Character):
    pass
