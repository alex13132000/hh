import pygame

import background
import player
import bullet


WIDTH, HEIGHT = 420, 720
TICK = 60

class Scene:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = background.Background(self.screen)
        self.player = player.Player(self.screen)
        self.bullets = []
        self.enemies = []
        self.enemy_bullets = []
        self.hp = []


    def update(self):
        self.background.update()
        self.player.update()

    def draw(self):
        self.background.draw()
        self.player.draw()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(TICK)

