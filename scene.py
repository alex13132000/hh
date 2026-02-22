import pygame

import background
import bullet
import player
import enemy


WIDTH, HEIGHT = 420, 720
TICK = 60
ENEMY_DELAY = 90

class Scene:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self._background = background.Background(self)
        self._clock = pygame.time.Clock()
        self._hp = []
        self._transients = []
        self._player = player.Player(self)
        self.last_enemy = 0

    def shoot(self):
        self._transients.append(
            bullet.Bullet(
                self, self._player.position_x, self._player.position_y
            )
        )

    def get_bullets(self):
        return [o for o in self._transients if isinstance(o, bullet.Bullet)]

    def _add_enemy(self):
        if self.last_enemy > ENEMY_DELAY:
            self._transients.append(enemy.Enemy(self))
            self.last_enemy = 0
        else:
            self.last_enemy += 1

    def remove_transient(self, transients):
        self._transients.remove(transients)

    def update(self):
        self._background.update()
        self._player.update()
        for b in self._transients:
            b.update()
        self._add_enemy()



    def draw(self):
        self._background.draw()
        self._player.draw()
        for b in self._transients:
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

