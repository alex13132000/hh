"""Модуль класса Player.
"""

import pygame

SHIP_IMAGE_FILE = 'assets/images/player_ship/player.png'
PLAYER_ZONE = (16, 368, 300, 684)
SPAWN = [200, 600]
SPEED = 5

class Player:
    """Корабль игрока.
        - Класс спрайта с позицией, движением (влево/вправо) и стрельбой.
        - Ограничение движения нижней частью экрана.
    """


    def __init__(self, screen):
        self.position_x = SPAWN[0]
        self.position_y = SPAWN[1]
        self.screen = screen
        self._spawn()
        self.image = pygame.image.load(SHIP_IMAGE_FILE)
        #self.rect = self.image.get_rect(topleft=(position_x, position_y))

    def _move(self, speed, axis='x'):
        saved_x, saved_y = self.position_x, self.position_y

        if axis == 'x':
            self.position_x += speed
        elif axis == 'y':
            self.position_y += speed

        # Ограничение зоны движения
        if not (
            PLAYER_ZONE[0] <= self.position_x <= PLAYER_ZONE[1] and
            PLAYER_ZONE[2] <= self.position_y <= PLAYER_ZONE[3]
        ):
            self.position_x, self.position_y = saved_x, saved_y

    def update(self):
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
        self.screen.blit(
            source=self.image,
            dest=(self.position_x, self.position_y),
        )
        
    def _spawn(self):
        self.position_y = 600
        self.position_x = 200