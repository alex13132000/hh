import pygame

import player_control


BG = "assets/images/BG/BG_1.png"


pygame.init()
screen = pygame.display.set_mode((420, 720))
clock = pygame.time.Clock()
running = True

player = player_control.Player(screen, 200, 200)


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(pygame.image.load(BG), (0, 0))
    player.input()
    player.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()