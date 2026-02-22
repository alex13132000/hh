import random

import pygame


IMG = 'assets/images/enemy_ship/enemy_simple.png'
SPEED = 5
SPAWN_Y = -25


class Enemy:
    def __init__(self, scene):
        self.scene = scene
        self.image = pygame.image.load(IMG)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(10, 401, 10)
        self.rect.y = SPAWN_Y

    def update(self):
        self.rect.y += SPEED
        if self.rect.y > self.scene.screen.get_height():
            self.scene.remove_transient(self)
        self._check_collision()

    def draw(self):
        self.scene.screen.blit(self.image, self.rect)

    def _check_collision(self):
        for b in self.scene.get_bullets():
            if self.rect.colliderect(b.rect):
                self.scene.remove_transient(b)
                self.scene.remove_transient(self)
