import pygame

import background
import bullet
import player


WIDTH, HEIGHT = 420, 720
TICK = 60


class Scene:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self._background = background.Background(self)
        self._bullets = []
        self._clock = pygame.time.Clock()
        self._enemies = []
        self._enemy_bullets = []
        self._hp = []
        self._player = player.Player(self)

    def shoot(self):
        self._bullets.append(
            bullet.Bullet(self, self._player.position_x, self._player.position_y)
        )

    def remove_bullet(self, bullet):
        self._bullets.remove(bullet)

    def update(self):
        self._background.update()
        self._player.update()
        for b in self._bullets:
            b.update()

    def draw(self):
        self._background.draw()
        self._player.draw()
        for b in self._bullets:
            b.draw()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.update()
            self.draw()
            pygame.display.flip()
            self._clock.tick(TICK)

