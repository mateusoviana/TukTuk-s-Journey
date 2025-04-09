import pygame
import random
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ui import display_message, create_button

def start_battle(hero, enemy, game):
    white = (255, 255, 255)

    hero.set_sprite('back_default')
    enemy.set_sprite('front_default')

    hero.x, hero.y = 0, 150
    enemy.x, enemy.y = 300, 0
    hero.size = enemy.size = 300

    hero.hp_x, hero.hp_y = 275, 250
    enemy.hp_x, enemy.hp_y = 50, 50

    game_status = 'start battle'

    while game_status != 'gameover':
        game.fill(white)

        if game_status == 'start battle':
            alpha = 0
            while alpha < 255:
                game.fill(white)
                enemy.draw(game, alpha)
                display_message(f'{enemy.name} apareceu!', game)
                alpha += .4
                pygame.display.update()
            time.sleep(1)
            alpha = 0
            while alpha < 255:
                game.fill(white)
                hero.draw(game, alpha)
                enemy.draw(game)
                display_message(f'Vai, {hero.name}!', game)
                alpha += .4
                pygame.display.update()
            game_status = 'player turn'

        elif game_status == 'player turn':
            fight_button = create_button(240, 140, 10, 350, 130, 412, 'Lutar')
            potion_button = create_button(240, 140, 250, 350, 370, 412, f'Poção ({hero.num_potions})')
            hero.draw(game)
            enemy.draw(game)
            hero.draw_hp(game)
            enemy.draw_hp(game)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = event.pos
                    if fight_button.collidepoint(mouse):
                        game_status = 'player move'
                    elif potion_button.collidepoint(mouse):
                        if hero.num_potions > 0:
                            hero.use_potion()
                            display_message(f'{hero.name} usou uma poção!', game)
                            time.sleep(2)
                        game_status = 'enemy turn'

        elif game_status == 'player move':
            move_buttons = []
            for i, move in enumerate(hero.moves):
                x = 10 + (i % 2) * 240
                y = 350 + (i // 2) * 70
                button = create_button(240, 70, x, y, x+120, y+35, move.name)
                move_buttons.append((button, move))
            hero.draw(game)
            enemy.draw(game)
            hero.draw_hp(game)
            enemy.draw_hp(game)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button, move in move_buttons:
                        if button.collidepoint(event.pos):
                            hero.perform_attack(enemy, move, game)
                            game_status = 'enemy turn' if enemy.current_hp > 0 else 'gameover'
                            break

        elif game_status == 'enemy turn':
            move = random.choice(enemy.moves)
            hero.draw(game)
            enemy.draw(game)
            hero.draw_hp(game)
            enemy.draw_hp(game)
            pygame.display.update()
            enemy.perform_attack(hero, move, game)
            time.sleep(1.5)
            game_status = 'player turn' if hero.current_hp > 0 else 'gameover'

        elif game_status == 'gameover':
            display_message('Fim da batalha!', game)
            pygame.display.update()
            time.sleep(3)
