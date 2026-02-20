"""Модуль класса Player.
"""

import pygame


IMG = 'assets/images/player_ship/player.png'
ZONE = (16, 368, 300, 684)
SPAWN = [200, 600]
SPEED = 5
SHOT_DELAY = 30


class Player:
    """Корабль игрока.
        - Класс спрайта с позицией, движением (влево/вправо) и стрельбой.
        - Ограничение движения нижней частью экрана.
    """
    def __init__(self, scene):
        self.last_shot = SHOT_DELAY
        self.position_x = SPAWN[0]
        self.position_y = SPAWN[1]
        self.scene = scene
        self._spawn()
        self.image = pygame.image.load(IMG)
        #self.rect = self.image.get_rect(topleft=(position_x, position_y))

    def _move(self, speed, axis='x'):
        saved_x, saved_y = self.position_x, self.position_y

        if axis == 'x':
            self.position_x += speed
        elif axis == 'y':
            self.position_y += speed

        # Ограничение зоны движения
        if not (
            ZONE[0] <= self.position_x <= ZONE[1] and
            ZONE[2] <= self.position_y <= ZONE[3]
        ):
            self.position_x, self.position_y = saved_x, saved_y

    def _shoot(self):
        if self.last_shot > SHOT_DELAY:
            self.scene.shoot()
            self.last_shot = 0

    def update(self):
        self.last_shot += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self._move(-SPEED, 'x')
        if keys[pygame.K_d]:
            self._move(SPEED, 'x')
        if keys[pygame.K_w]:
            self._move(-SPEED, 'y')
        if keys[pygame.K_s]:
            self._move(SPEED, 'y')
        if keys[pygame.K_SPACE]:
            self._shoot()

    def draw(self):
        # Отрисовка корабля игрока на экране
        self.scene.screen.blit(
            source=self.image,
            dest=(self.position_x, self.position_y),
        )

    def _spawn(self):
        self.position_y = 600
        self.position_x = 200

