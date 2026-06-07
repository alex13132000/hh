import math

import pygame

import blast


PARTS = 3
POINTS = 4


class BaseEnemy:
    def __init__(self, scene, image_filename, trajectory, fly_time):
        self.scene = scene
        self.image = pygame.image.load(image_filename)
        self.trajectory = trajectory
        self.fly_time = fly_time
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
            u**3 * p0[0] +
            3*u**2*t * p1[0] +
            3*u*t**2 * p2[0] +
            t**3 * p3[0],
            u**3 * p0[1] +
            3*u**2*t * p1[1] +
            3*u*t**2 * p2[1] +
            t**3 * p3[1]
        )

    @staticmethod
    def get_orientation_angle(p0, p1, p2, p3, t):
        u = 1 - t
        dx = (
            3*u*u*(p1[0] - p0[0]) +
            6*u*t*(p2[0] - p1[0]) +
            3*t*t*(p3[0] - p2[0])
        )
        dy = (
            3*u*u*(p1[1] - p0[1]) +
            6*u*t*(p2[1] - p1[1]) +
            3*t*t*(p3[1] - p2[1])
        )
        return -math.degrees(math.atan2(dy, dx))

    def update(self):
        now = pygame.time.get_ticks()
        age = now - self.spawn
        part, delta_t = divmod(age, self.fly_time)
        if part >= PARTS:
            self.scene.transients.remove(self)
            return
        points = (
            self.trajectory[
                part*(POINTS-1):part*(POINTS-1)+POINTS
            ]
        )
        self.rect.center = self.get_abs_pos(
            self.get_bezier_point(*points, delta_t / self.fly_time)
        )
        self.rotated_image = pygame.transform.rotate(
            self.image, self.get_orientation_angle(
                *points, delta_t / self.fly_time
            )
        )
        self._check_collision_bullets()
        self._check_collision_player()

    def draw(self):
        self.scene.screen.blit(self.rotated_image, self.rect)

    def _check_collision_bullets(self):
        for b in self.scene.get_bullets():
            if self.rect.colliderect(b.rect):
                self.scene.transients.remove(b)
                self.scene.transients.remove(self)
                self.scene.score.score += 1
                blast.Blast(self.scene, self.rect)


    def _check_collision_player(self):
        if self.rect.colliderect(self.scene.player.rect):
            self.scene.transients.remove(self)
            self.scene.hearts.hp -= 1
            blast.Blast(self.scene, self.rect)


class SCurveRaiderI(BaseEnemy):
    def __init__(self, scene):
        super().__init__(
            scene=scene,
            image_filename='assets/images/enemy_ship/enemy_simple.png',
            trajectory=(
                (.2, -.1),
                (.1, .2),
                (.2, .4),
                (.3, .5),
                (.4, .6),
                (.5, .7),
                (.6, .8),
                (.7, .9),
                (.6, 1.0),
                (.7, 1.2),
            ),
            fly_time=2000,
        )

class SCurveTankI(BaseEnemy):
    def __init__(self, scene):
        super().__init__(
            scene=scene,
            image_filename='assets/images/enemy_ship/enemy_big.png',
            trajectory=(
                (.8, -.1),
                (.9, .2),
                (.8, .4),
                (.7, .5),
                (.6, .6),
                (.5, .7),
                (.4, .8),
                (.3, .9),
                (.4, 1.0),
                (.3, 1.2),
            ),
            fly_time=4000,
        )

class SCurveSpeedI(BaseEnemy):
    def __init__(self, scene):
        super().__init__(
            scene=scene,
            image_filename='assets/images/enemy_ship/enemy_speed.png',
            trajectory=(
                (.1, -.1),
                (.0, .2),
                (.3, .4),
                (.5, .6),
                (.7, .5),
                (.9, .4),
                (1, .3),
                (.9, .8),
                (.7, 1),
                (.5, 1.2),
            ),
            fly_time=1500,
        )
