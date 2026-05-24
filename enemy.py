import random

import pygame


IMG = 'assets/images/enemy_ship/enemy_simple.png'
SPEED = 5
SPAWN_Y = -25


class Enemy:
    def __init__(self, scene, enemy_data):
        self.scene = scene
        self.image = pygame.image.load(IMG)
        self.rect = self.image.get_rect()
        self.rect.move_ip(random.randrange(10, 401, 10), SPAWN_Y)
        self.enemy_delay = 1.5
        self.enemy_data = enemy_data
        self.path_all = ['entry_path', 'attack_path', 'exit_path']
        self.current_path = 0
        self.ttl = 2000
        self.start_time = None
        self.control_points = []
        self.load_current_path()
        self.start_time = pygame.time.get_ticks()

    def load_current_path(self):
        if self.current_path_index >= len(self.path_all):
            self.scene.remove_transient(self)
            return
        path_name = self.path_all[self.current_path_index]
        raw_points = self.enemy_data[path_name]['control_points']
        screen_w = self.scene.screen.get_width()
        screen_h = self.scene.screen.get_height()
        self.control_points = [
            (p['x']*screen_w, p['y']*screen_h) for p in raw_points
            ]
        
    @staticmethod
    def bezier_point(p0, p1, p2, p3, t):
        u = 1 - t
        return (
        u**3 * p0[0] + 3*u**2*t * p1[0] + 3*u*t**2 * p2[0] + t**3 * p3[0],
        u**3 * p0[1] + 3*u**2*t * p1[1] + 3*u*t**2 * p2[1] + t**3 * p3[1]
    )
        



    def update(self):
        if self.start_time == None:
            return
        elapsed = pygame.time.get_ticks() - self.start_time
        t = elapsed / self.ttl
        if t >= 1.0:
            self.current_path_index += 1
            self.load_current_path()
            return
        if len(self.control_points) == 4:
            new_x, new_y = self.bezier_point(*self.control_points, t)
            self.rect.center = (new_x, new_y)
        #self.rect.y += SPEED
        #if self.rect.y > self.scene.screen.get_height():
            #self.scene.remove_transient(self)
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

