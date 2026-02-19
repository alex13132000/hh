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
        self.bullet = bullet.Bullet(self.player.position_x, self.player.position_y, self.screen)
        self.bullets = []
        self.enemies = []
        self.enemy_bullets = []
        self.hp = []


    def update(self):
        self.background.update()
        self.player.update()
        self.bullet.update()

    def draw(self):
        self.background.draw()
        self.player.draw()
        if pygame.key.get_pressed(pygame.K_SPACE):
            b = bullet.Bullet(self.player.position_x, self.player.position_y, self.screen)
            self.bullets.append(b)
            for b in self.bullets:
                b.draw(self.screen)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(TICK)

