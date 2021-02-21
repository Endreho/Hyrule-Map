from __future__ import division
import pygame, sys
import os.path
import pygame.freetype
import pygame.font

Running = True

class Player(pygame.sprite.DirtySprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Launch_animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load('images/image0.png'))
        self.sprites.append(pygame.image.load('images/image1.png'))
        self.sprites.append(pygame.image.load('images/image2.png'))
        self.sprites.append(pygame.image.load('images/image3.png'))
        self.sprites.append(pygame.image.load('images/image4.png'))
        self.sprites.append(pygame.image.load('images/image5.png'))
        self.sprites.append(pygame.image.load('images/image6.png'))
        self.sprites.append(pygame.image.load('images/image7.png'))
        self.sprites.append(pygame.image.load('images/image8.png'))
        self.sprites.append(pygame.image.load('images/image9.png'))
        self.sprites.append(pygame.image.load('images/image10.png'))
        self.sprites.append(pygame.image.load('images/image11.png'))
        self.sprites.append(pygame.image.load('images/image12.png'))
        self.sprites.append(pygame.image.load('images/image13.png'))
        self.sprites.append(pygame.image.load('images/image14.png'))
        self.sprites.append(pygame.image.load('images/image15.png'))
        self.sprites.append(pygame.image.load('images/image16.png'))
        self.sprites.append(pygame.image.load('images/image17.png'))
        self.sprites.append(pygame.image.load('images/image18.png'))
        self.sprites.append(pygame.image.load('images/image19.png'))
        self.sprites.append(pygame.image.load('images/image20.png'))
        self.sprites.append(pygame.image.load('images/image21.png'))
        self.sprites.append(pygame.image.load('images/image22.png'))
        self.sprites.append(pygame.image.load('images/image23.png'))
        self.sprites.append(pygame.image.load('images/image24.png'))
        self.sprites.append(pygame.image.load('images/image25.png'))
        self.sprites.append(pygame.image.load('images/image26.png'))
        self.sprites.append(pygame.image.load('images/image27.png'))
        self.sprites.append(pygame.image.load('images/image28.png'))
        self.sprites.append(pygame.image.load('images/image29.png'))
        self.sprites.append(pygame.image.load('images/image30.png'))
        self.sprites.append(pygame.image.load('images/image31.png'))
        self.sprites.append(pygame.image.load('images/image32.png'))
        self.sprites.append(pygame.image.load('images/image33.png'))
        self.sprites.append(pygame.image.load('images/image34.png'))
        self.sprites.append(pygame.image.load('images/image35.png'))
        self.sprites.append(pygame.image.load('images/image36.png'))
        self.sprites.append(pygame.image.load('images/image37.png'))
        self.sprites.append(pygame.image.load('images/image38.png'))
        self.sprites.append(pygame.image.load('images/image39.png'))
        self.sprites.append(pygame.image.load('images/image40.png'))
        self.sprites.append(pygame.image.load('images/image41.png'))
        self.sprites.append(pygame.image.load('images/image42.png'))
        self.sprites.append(pygame.image.load('images/image43.png'))
        self.sprites.append(pygame.image.load('images/image44.png'))
        self.sprites.append(pygame.image.load('images/image45.png'))
        self.sprites.append(pygame.image.load('images/image46.png'))
        self.sprites.append(pygame.image.load('images/image47.png'))
        self.sprites.append(pygame.image.load('images/image48.png'))
        self.sprites.append(pygame.image.load('images/image49.png'))
        self.sprites.append(pygame.image.load('images/image50.png'))
        self.sprites.append(pygame.image.load('images/image51.png'))
        self.sprites.append(pygame.image.load('images/image52.png'))
        self.sprites.append(pygame.image.load('images/image53.png'))
        self.sprites.append(pygame.image.load('images/image54.png'))
        self.sprites.append(pygame.image.load('images/image55.png'))
        self.sprites.append(pygame.image.load('images/image56.png'))
        self.sprites.append(pygame.image.load('images/image57.png'))
        self.sprites.append(pygame.image.load('images/image58.png'))
        self.sprites.append(pygame.image.load('images/image59.png'))
        self.sprites.append(pygame.image.load('images/image60.png'))
        self.sprites.append(pygame.image.load('images/image61.png'))
        self.sprites.append(pygame.image.load('images/image62.png'))
        self.sprites.append(pygame.image.load('images/image63.png'))
        self.sprites.append(pygame.image.load('images/image64.png'))
        self.sprites.append(pygame.image.load('images/image65.png'))
        self.sprites.append(pygame.image.load('images/image66.png'))
        self.sprites.append(pygame.image.load('images/image67.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x + 1024/2, pos_y + 600/2]

    def attack(self):
        self.Launch_animation = True

    def update(self, speed):
        if self.Launch_animation == True:
            self.current_sprite += speed

        if self.current_sprite < 68:
            self.image = self.sprites[int(self.current_sprite)]


# General setup
pygame.init()
clock = pygame.time.Clock()
GAME_FONT = pygame.freetype.Font("Calamity-Bold.otf", 19.4068)
GAME_FONT_OUTLINE = pygame.freetype.Font("Calamity-Bold.otf", 24.2+1.3281472327365)
Central_Hyrule = pygame.image.load('Asset 1.png')

# Game Screen
screen_width = 1024
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sheikah Slate")
world_offset = [0,-150]
width=256 #original image size
height=256
posx=128 #original display center, relative to the image
posy=128



# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(-(1024 / 2), -300)
moving_sprites.add(player)
hyrule = pygame.image.load('Map over Hyrule (3).png')
zoom_event = False
scale_up = 1.2
scale_down = 0.8


class GameState:
    def __init__(self):
        self.tab = 1
        self.zoom = 1
        self.world_offset_x = 0
        self.world_offset_y = 0
        self.update_screen = True
        self.panning = False
        self.pan_start_pos = None
        self.legacy_screen = pygame.Surface((screen_width, screen_height))

game_state = GameState()


def world_2_screen(world_x, world_y):
    screen_x = (world_x - game_state.world_offset_x) * game_state.zoom
    screen_y = (world_y - game_state.world_offset_y) * game_state.zoom
    return [screen_x, screen_y]


def screen_2_world(screen_x, screen_y):
    world_x = (screen_x / game_state.zoom) + game_state.world_offset_x
    world_y = (screen_y / game_state.zoom) + game_state.world_offset_y
    return [world_x, world_y]


def central_hyrule(x,y):
    screen.blit(Central_Hyrule, (x,y))

Quit = False


while not Quit:

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_state.tab == 1:
                    game_state.tab = 2
                elif game_state.tab == 2:
                    game_state.tab = 1


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 or event.button == 5:
                # X and Y before the zoom
                mouseworld_x_before, mouseworld_y_before = screen_2_world(mouse_x, mouse_y)

                # ZOOM IN/OUT
                if event.button == 4 and game_state.zoom < 10:
                    game_state.zoom *= scale_up
                    print('Zoomed in')
                elif event.button == 5 and game_state.zoom > 0.5:
                    game_state.zoom *= scale_down

                # X and Y after the zoom
                mouseworld_x_after, mouseworld_y_after = screen_2_world(mouse_x, mouse_y)

                # Do the difference between before and after, and add it to the offset
                game_state.world_offset_x += mouseworld_x_before - mouseworld_x_after
                game_state.world_offset_y += mouseworld_y_before - mouseworld_y_after

            elif event.button == 2:
                # PAN START
                game_state.panning = True
                game_state.pan_start_pos = mouse_x, mouse_y


            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 2 and game_state.panning:
                    # PAN STOP
                    game_state.panning = False

            if game_state.panning:
                # Pans the screen if the left mouse button is held
                game_state.world_offset_x -= (mouse_x - game_state.pan_start_pos[0]) / game_state.zoom
                game_state.world_offset_y -= (mouse_y - game_state.pan_start_pos[1]) / game_state.zoom
                game_state.pan_start_pos = mouse_x, mouse_y
                print(mouse_x, mouse_y)

        if Running:
           player.attack()

    central_hyrule(416, 260)
    screen.blit(hyrule, (0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update(.5)
    pygame.display.flip()
    clock.tick(60)
