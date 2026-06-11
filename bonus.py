import random

import pygame

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
        self.rect.y += SPEED
        if self.rect.y > BOUNDARY + self.scene.screen.get_height():
            self.scene.transients.remove(self)

    def draw(self):
        self.scene.screen.blit(source=self.image, dest=self.rect)


class BonusBomb(BaseBonus):
    def __init__(self, scene):
        super().__init__(
            scene=scene,
            image_filename='assets/images/bonus_ship/bonus_bomb.png',
        )

    def _check_collision_player(self):
        if self.rect.colliderect(self.scene.player.rect):
            self.scene.transients.remove(self)
