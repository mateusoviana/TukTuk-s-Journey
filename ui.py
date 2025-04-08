import pygame

def display_message(message, game):
    white = (255, 255, 255)
    black = (0, 0, 0)
    pygame.draw.rect(game, white, (10, 350, 480, 140))
    pygame.draw.rect(game, black, (10, 350, 480, 140), 3)

    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    text = font.render(message, True, black)
    text_rect = text.get_rect()
    text_rect.x = 30
    text_rect.y = 410
    game.blit(text, text_rect)

    pygame.display.update()

def create_button(width, height, left, top, text_cx, text_cy, label):
    mouse_cursor = pygame.mouse.get_pos()
    button = pygame.Rect(left, top, width, height)
    white = (255, 255, 255)
    gold = (218, 165, 32)
    black = (0, 0, 0)

    screen = pygame.display.get_surface()

    if button.collidepoint(mouse_cursor):
        pygame.draw.rect(screen, gold, button)
    else:
        pygame.draw.rect(screen, white, button)

    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render(f'{label}', True, black)
    text_rect = text.get_rect(center=(text_cx, text_cy))
    screen.blit(text, text_rect)

    return button
