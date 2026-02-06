import pygame

from scene import Scene

pygame.init()
screen = pygame.display.set_mode((420, 720))
clock = pygame.time.Clock()

scene = Scene(screen)

is_running = True
while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    bg.update()
    bg.draw()
    player.input()
    player.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()