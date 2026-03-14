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
        self.rect.move_ip(random.randrange(10, 401, 10), SPAWN_Y)

    def update(self):
        self.rect.y += SPEED
        if self.rect.y > self.scene.screen.get_height():
            self.scene.remove_transient(self)
        self._check_collision_bullets()
        self._check_collision_player()

    def draw(self):
        self.scene.screen.blit(self.image, self.rect)

    def _check_collision_bullets(self):
        for b in self.scene.get_bullets():
            if self.rect.colliderect(b.rect):
                self.scene.remove_transient(b)
                self.scene.remove_transient(self)
                self.scene.score.score += 1

    def _check_collision_player(self):
        if self.rect.colliderect(self.scene.player.rect):
            self.scene.remove_transient(self)
            self.scene.hearts.hp -= 1
            if self.scene.hearts.hp == 0:
                pygame.quit()






