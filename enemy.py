import random

import pygame


IMG = 'assets/images/enemy_ship/enemy_simple.png'
FLY_TIME = 2000
TRAJECTORY = [
    (-.2, .9),
    (.2, .7),
    (-.1, .5),
    (.3, .3),
    (.6, .5),
    (.4, .8),
    (.5, 1.1),
    (.8, 1.2),
    (1.1, 1),
    (1.1, 1),
]
PARTS = 3
POINTS = 4


class Enemy:
    def __init__(self, scene):
        self.scene = scene
        self.image = pygame.image.load(IMG)
        self.rect = self.image.get_rect()
        self.spawn = pygame.time.get_ticks()

    def get_abs_pos(self, rel_pos):
        return (
            rel_pos[0] * self.scene.screen.get_width(),
            rel_pos[1] * self.scene.screen.get_height(),
        )

    @staticmethod
    def get_bezier_point(p0, p1, p2, p3, t):
        u = 1 - t
        return (
            u**3 * p0[0] + 3*u**2*t * p1[0] + 3*u*t**2 * p2[0] + t**3 * p3[0],
            u**3 * p0[1] + 3*u**2*t * p1[1] + 3*u*t**2 * p2[1] + t**3 * p3[1]
        )

    def update(self):
        now = pygame.time.get_ticks()
        age = now - self.spawn
        index, delta_t = divmod(age, FLY_TIME)
        if index >= PARTS:
            return
        points = (
            TRAJECTORY[index*PARTS:index*PARTS+POINTS]
        )
        self.rect.center = self.get_abs_pos(
            self.get_bezier_point(*points, delta_t / FLY_TIME)
        )
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

