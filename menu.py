import pygame
import pygame_menu
from pygame_menu import themes

# Inicializando o Pygame
pygame.init()

# Configuração da tela
surface = pygame.display.set_mode((480, 480))

# Carregar os sprites

background_sprite = pygame.image.load('battle/sprites/back_menu.png')  # Substitua pelo caminho do seu sprite de fundo

# Ajustar tamanho dos sprites, se necessário

background_sprite = pygame.transform.scale(background_sprite, (480, 480))  # O fundo pode cobrir toda a tela


# Função para iniciar o jogo
def start_the_game():
    global game_started
    game_started = True  # Marca que o jogo foi iniciado

# Criando o menu principal com as opções "Play" e "Quit"
mainmenu = pygame_menu.Menu('A Jornada de TukTuk', 480, 480, theme= themes.THEME_DARK)
mainmenu.add.button('Play', start_the_game)  # Botão Play que chama a função start_the_game
mainmenu.add.button('Quit', pygame_menu.events.EXIT)  # Botão para sair do jogo

# Função principal que exibe o menu e aguarda a interação do usuário
def show_menu():
    global game_started
    game_started = False  # Inicialmente o jogo não está iniciado

    # Laço para mostrar o menu até que o jogador clique em "Play"
    while not game_started:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  # Fecha o Pygame se o usuário clicar para fechar a janela

        mainmenu.update(events)  # Atualiza o menu

        mainmenu.draw(surface)  # Desenha o menu na tela

        surface.blit(background_sprite, (0, 0))  # Desenha o fundo na tela

        # Desenha o sprite do TukTuk em uma posição específica
        
        pygame.display.update()  # Atualiza a tela

    return game_started  # Retorna True quando o jogo deve começar

# Chama a função para exibir o menu
show_menu()