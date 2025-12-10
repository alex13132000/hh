import pygame

import player_control

pygame.init()
screen = pygame.display.set_mode((420, 720))
clock = pygame.time.Clock()
running = True

player = player_control.Player(screen, 200, 200)


while running:

    player.draw

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")
    pygame.display.flip()
    clock.tick(60)

pygame.quit()