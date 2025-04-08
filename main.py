import pygame
from game import Game
from config import TILE_SIZE

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()

    pygame.display.set_caption("A Jornada de TukTuk")
    window = pygame.display.set_mode((32*TILE_SIZE, 20*TILE_SIZE))
    clock = pygame.time.Clock()

    game = Game(window, clock)
    game.run()

    pygame.quit()