import pygame, time, random
from pygame.locals import *
from pytmx.util_pygame import load_pygame

def blit_all_tiles(window, tmxdata, world_offset):
    for layer in tmxdata:
        for tile in layer.tiles():
            # tile[0] .... x grid location
            # tile[1] .... y grid location
            # tile[2] .... image data for blitting
            img = pygame.transform.scale(tile[2], (16,16))
            x_pixel = tile[0] * 16 + world_offset[0]
            y_pixel = tile[1] * 16 + world_offset[1]
            window.blit(img, (x_pixel, y_pixel))

def get_tile_properties(tmxdata, x, y, worldoffset):
    world_x = x - worldoffset[0]
    world_y = y - worldoffset[1]
    tile_x = world_x // 16
    tile_y = world_y // 16
    properties = tmxdata.get_tile_properties(tile_x, tile_y, 0)
    if properties is None:
        properties = {"solid":0}
    return properties

def main():
    # ********** Game variables **********
    tmxdata = load_pygame("assets/Tileset1/map1.tmx")
    y_ground = window.get_height() - 16
    quit = False
    x = 64
    y = y_ground - 64
    # Standing still
    player_stand = pygame.image.load("assets/p3/p3_stand.png").convert_alpha()
    player_stand = pygame.transform.scale(player_stand, (16, 16))
    # Jumping
    player_jump = pygame.image.load("assets/p3/p3_jump.png").convert_alpha()
    player_jump = pygame.transform.scale(player_jump, (16, 16))
    # Ducking
    player_duck = pygame.image.load("assets/p3/p3_duck.png").convert_alpha()
    player_duck = pygame.transform.scale(player_duck, (16, 16))
    # Moving right
    player_right = [
        pygame.image.load("assets/p3/PNG/p3_walk01.png").convert_alpha(),
        pygame.image.load("assets/p3/PNG/p3_walk02.png").convert_alpha(),
        pygame.image.load("assets/p3/PNG/p3_walk03.png").convert_alpha(),
        pygame.image.load("assets/p3/PNG/p3_walk04.png").convert_alpha(),
        pygame.image.load("assets/p3/PNG/p3_walk05.png").convert_alpha(),
        pygame.image.load("assets/p3/PNG/p3_walk06.png").convert_alpha(),
        pygame.image.load("assets/p3/PNG/p3_walk07.png").convert_alpha(),
        pygame.image.load("assets/p3/PNG/p3_walk08.png").convert_alpha(),
        pygame.image.load("assets/p3/PNG/p3_walk09.png").convert_alpha(),
        pygame.image.load("assets/p3/PNG/p3_walk10.png").convert_alpha(),
        pygame.image.load("assets/p3/PNG/p3_walk11.png").convert_alpha(),
    ]
    # Resize all images in the list to 16x16
    player_right = [pygame.transform.scale(image, (16,16)) for image in player_right]
    # Variable to remember which frame from the list we last displayed
    player_right_frame = 0
    # Create moving images by flipping the right facing images on the horizontal axis
    player_left = [pygame.transform.flip(image, True, False) for image in player_right]
    player_left_frame = 0
    # Maintain our direction
    direction = "stand"
    world_offset = [0,0]

    # ********** Start game loop **********
    while not quit:
        window.fill((64,64,64))                                 # Reset screen to black
        blit_all_tiles(window, tmxdata, world_offset)
        # ********** Process events **********
        keyspressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            print(event)      # Useful debugging tip
            if event.type == QUIT:
                quit = True

        if keyspressed[ord("a")]:
            direction = "left"
            if x > 16:
                left_block = get_tile_properties(tmxdata, x - 16, y, world_offset)
                if left_block['solid'] == 0:
                    x = x - 16

        if keyspressed[ord("d")]:
            direction = "right"
            if x < window.get_width() - 32:
                right_block = get_tile_properties(tmxdata, x + 16, y, world_offset)
                if right_block['solid'] == 0:
                    x = x + 16

        if keyspressed[ord("w")]:
            direction = "up"
            if y > 16:
                up_block = get_tile_properties(tmxdata, x, y - 16, world_offset)
                if up_block['solid'] == 0:
                    y = y - 16

        if keyspressed[ord("s")]:
            direction = "down"
            if y < window.get_height() - 32:
                down_block = get_tile_properties(tmxdata, x, y + 16, world_offset)
                if down_block['solid'] == 0:
                    y = y + 16

        if sum(keyspressed) == 0:
            direction = "stand"

        # Keep player within screen limits
        if x < 0:
            x = 0
            # world_offset[0] += 16
        if x > window.get_width() - 16:
            x = window.get_width() - 16
            # world_offset[0] -= 16
        if y < 0:
            y = 0
            # world_offset[1] += 16
        if y > y_ground:
            y = y_ground
            # world_offset[1] -= 16

        # ********** Your game logic here **********

        if direction == "stand":
            window.blit(player_stand, (x, y))
        elif direction == "up":
            window.blit(player_jump, (x,y))
        elif direction == "down":
            window.blit(player_duck, (x,y))
        elif direction == "right":
            window.blit(player_right[player_right_frame], (x,y))
            player_right_frame = (player_right_frame + 1) % len(player_right)
        elif direction == "left":
            window.blit(player_left[player_left_frame], (x,y))
            player_left_frame = (player_left_frame + 1) % len(player_left)

        # ********** Update screen **********
        pygame.display.update()                                # Actually does the screen update
        clock.tick(15)                                         # Run the game at 25 frames per second

if __name__ == "__main__":
    width, height = 640, 640
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("A Jornada de TukTuk")
    window = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    main()
    pygame.quit()