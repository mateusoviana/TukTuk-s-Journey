import pygame
from character import Hero, Enemy
from data import CHARACTER_DATA
from battle import start_battle


def main():
    pygame.init()
    global game
    game = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('RPG Battle System')

    white = (255, 255, 255)
    running = True

    while running:
        game.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                hero = Hero("TukTuk", CHARACTER_DATA['tuktuk'], level=30, x=0, y=0)
                if event.key == pygame.K_w:
                    enemy = Enemy("Water Boss", CHARACTER_DATA['water_boss'], level=25, x=0, y=0)
                    start_battle(hero, enemy, game)
                elif event.key == pygame.K_f:
                    enemy = Enemy("Fire Boss", CHARACTER_DATA['fire_boss'], level=25, x=0, y=0)
                    start_battle(hero, enemy, game)
                elif event.key == pygame.K_e:
                    enemy = Enemy("Earth Boss", CHARACTER_DATA['earth_boss'], level=25, x=0, y=0)
                    start_battle(hero, enemy, game)
                elif event.key == pygame.K_d:
                    enemy = Enemy("Wind Boss", CHARACTER_DATA['wind_boss'], level=25, x=0, y=0)
                    start_battle(hero, enemy, game)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
