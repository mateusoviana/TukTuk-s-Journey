import pygame
import pygame_menu
from pygame_menu import themes, baseimage, widgets

# Inicializando o Pygame
pygame.init()

# Configuração da tela
surface = pygame.display.set_mode((480, 480))

# Carregar os sprites

background_sprite = pygame.image.load('battle/sprites/menu_background.png')  # Substitua pelo caminho do seu sprite de fundo

# Ajustar tamanho dos sprites, se necessário

background_sprite = pygame.transform.scale(background_sprite, (480, 480))  # O fundo pode cobrir toda a tela


# Função para iniciar o jogo
def start_the_game():
    global game_started
    game_started = True  # Marca que o jogo foi iniciado

# Criando o menu principal com as opções "Play" e "Quit"
custom_theme = themes.THEME_DARK.copy()
custom_theme.background_color = baseimage.BaseImage(
    image_path='battle/sprites/menu_background.png',
    drawing_mode=baseimage.IMAGE_MODE_FILL
)

custom_theme.title_bar_style = widgets.MENUBAR_STYLE_NONE

mainmenu = pygame_menu.Menu('', 480, 480, theme=custom_theme)
play_button = mainmenu.add.button('Play', start_the_game)
quit_button = mainmenu.add.button('Quit', pygame_menu.events.EXIT)

play_button.set_position(50, 420)
quit_button.set_position(350, 420)

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


        # Desenha o sprite do TukTuk em uma posição específica
        
        pygame.display.update()  # Atualiza a tela

    return game_started  # Retorna True quando o jogo deve começar