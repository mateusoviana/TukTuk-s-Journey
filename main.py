import pygame
from game import Game
from config import TILE_SIZE

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()

    pygame.display.set_caption("A Jornada de TukTuk")
    window = pygame.display.set_mode((30*TILE_SIZE, 30*TILE_SIZE))
    clock = pygame.time.Clock()

    game = Game(window, clock)
    game.map_manager.set_game(game)
    game.run()

    pygame.quit()