import random

import pygame

from enemy import BaseEnemy

SPEED = 5
BOUNDARY = 50
MARGIN = 20

class BaseBonus:
    def __init__(self, scene, image_filename):
        self.scene = scene
        self.image = pygame.image.load(image_filename)
        self.rect = self.image.get_rect()
        self.rect.center = random.randint(
            MARGIN, scene.screen.get_width() - MARGIN
        ), -BOUNDARY
        self.scene.transients.append(self)

    def update(self):
        self._move()
        if self._is_eol() or self._is_player_collision():
            return

    def _move(self):
        self.rect.y += SPEED

    def draw(self):
        self.scene.screen.blit(source=self.image, dest=self.rect)

    def _is_eol(self):
        if self.rect.y > BOUNDARY + self.scene.screen.get_height():
            self.scene.transients.remove(self)
            return True

    def _is_player_collision(self):
        if self.rect.colliderect(self.scene.player.rect):
            self.scene.transients.remove(self)
            return True

class BonusBomb(BaseBonus):
    def __init__(self, scene):
        super().__init__(
            scene=scene,
            image_filename='assets/images/bonus_ship/bonus_bomb.png',
        )

    def _is_player_collision(self):
        if super()._is_player_collision():
            self.scene.transients = [
                i for i in self.scene.transients if not isinstance(i, BaseEnemy)
            ]
            return True

