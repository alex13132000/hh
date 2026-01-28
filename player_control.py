"""Модуль класса Player.
"""

import pygame

PLAYER_BULLET = 'assets/images/player_ship/bullet_P.png'
SHIP_IMAGE_FILE = 'assets/images/player_ship/player.png'
PLAYER_ZONE = (16, 368, 300, 684)


class Player:
    """Корабль игрока.
        - Класс спрайта с позицией, движением (влево/вправо) и стрельбой.
        - Ограничение движения нижней частью экрана.
    """

    position_x = 200
    position_y = 600
    image = None
    screen = None
    speed = 5
    player_rect = (position_x, position_y, 36, 36)

    def __init__(self, screen, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
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

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self._move(-self.speed, 'x')
        if keys[pygame.K_d]:
            self._move(self.speed, 'x')
        if keys[pygame.K_w]:
            self._move(-self.speed, 'y')
        if keys[pygame.K_s]:
            self._move(self.speed, 'y')

    def shoot(self, image_bullet = pygame.image.load(PLAYER_BULLET), speed_bullet = 10):
        self.speed_bullet = speed_bullet
        self.image_bullet = image_bullet

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.screen.blit(
            source=self.image_bullet,
            dest=(self.position_x+4, self.position_y-18),
        )


    def draw(self):
        # Отрисовка корабля игрока на экране
        self.screen.blit(
            source=self.image,
            dest=(self.position_x, self.position_y),
        )

    def _spawn(self):
        self.position_y = 600
        self.position_x = 200