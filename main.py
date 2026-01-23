import pygame

import background
import player_control



#BG = "assets/images/BG/BG_1.png"
# Закончить коструктор класса Background из background.py и использовать его здесь
# Конструктор должен грузить фон
# Метод draw - рисовать его на экран каждый кадр
# В этом же файле main.py создать объект Background и использовать его для отрисовки фона


pygame.init()

screen = pygame.display.set_mode((420, 720))
clock = pygame.time.Clock()
running = True

player = player_control.Player(screen, 200, 200)
bg = background.Background(screen)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    bg.update()
    bg.draw()
    player.input()
    player.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()