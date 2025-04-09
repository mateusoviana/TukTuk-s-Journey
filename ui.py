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

def display_message_1(message, game):
    # Cria uma nova janela para a mensagem
    window_width = 300
    window_height = 150
    message_window = pygame.Surface((window_width, window_height))
    message_window.fill((217,135,25))
    
    # Configura a fonte e o padding
    font = pygame.font.Font(None, 28) # Fonte menor para caber mais texto
    padding = 20
    max_width = window_width - 2 * padding
    
    # Lógica para quebrar o texto em linhas
    words = message.split(' ')
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] < max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line) # Adiciona a última linha

    # Desenha as linhas de texto
    y_offset = padding
    for line in lines:
        text = font.render(line.strip(), True, (0, 0, 0))
        text_rect = text.get_rect(center=(window_width // 2, y_offset + font.get_height() // 2))
        message_window.blit(text, text_rect)
        y_offset += font.get_height() + 5 # Espaçamento entre linhas
    
    # Desenha um botão de fechar (ajusta a posição y)
    button_y = max(y_offset + 10, window_height - 40) # Garante que o botão não sobreponha o texto
    close_button = pygame.Rect(100, button_y, 100, 30) 
    pygame.draw.rect(message_window, (234,234,174), close_button)
    close_font = pygame.font.Font(None, 30) # Fonte ligeiramente menor para o botão
    close_text = close_font.render("Fechar", True, (0, 0, 0))
    close_text_rect = close_text.get_rect(center=close_button.center)
    message_window.blit(close_text, close_text_rect)
    
    # Posiciona a janela no centro da tela
    window_rect = message_window.get_rect(center=game.get_rect().center)
    
    # Loop para manter a janela aberta
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Ajusta a verificação da colisão para a posição relativa da janela
                relative_mouse_pos = (mouse_pos[0] - window_rect.x, mouse_pos[1] - window_rect.y)
                if close_button.collidepoint(relative_mouse_pos):
                    waiting = False
            elif event.type == pygame.QUIT:
                waiting = False
                pygame.quit() # Fecha o jogo se a janela principal for fechada
                exit()
        
        # Desenha a janela de mensagem na tela principal do jogo
        game.blit(message_window, window_rect)
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
