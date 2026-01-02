"""Модуль класса Player.
"""

import pygame


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

    def __init__(self, screen, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.screen = screen
        self._load_image()
        self._spawn()

    def _move(self, speed, axis='h'):
        saved = self.position_x, self.position_y
        if axis == 'h':
            coords = self.position_x
        else:
            coords = self.position_y
        coords += self.speed
        if (
            self.position_x < PLAYER_ZONE[0] and
            self.position_x > PLAYER_ZONE[1] and
            self.position_y < PLAYER_ZONE[2] and
            self.position_y > PLAYER_ZONE[3]
        ):
            pass
        else:
            self.position_x, self.position_y = saved

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


    def move_right(self):
        ...

    def move_left(self):
        ...

    def move_up(self):
        ...

    def move_down(self):
        ...

    def shoot(self):
        ...

    def _load_image(self):
        self.image = pygame.image.load(SHIP_IMAGE_FILE)

    def draw(self):
        # Отрисовка корабля игрока на экране
        self.screen.blit(
            source=self.image,
            dest=(self.position_x, self.position_y),
        )

    def _spawn(self):
        self.position_y = 600
        self.position_x = 200