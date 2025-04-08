import pygame
from game import Game

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("A Jornada de TukTuk")
    window = pygame.display.set_mode((510, 320))
    clock = pygame.time.Clock()

    game = Game(window, clock)
    game.run()

    pygame.quit()