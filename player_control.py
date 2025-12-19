"""Модуль класса Player.
"""

import pygame


SHIP_IMAGE_FILE = 'assets/images/player_ship/player.png'

class Player:
    """Корабль игрока.
        - Класс спрайта с позицией, движением (влево/вправо) и стрельбой.
        - Ограничение движения нижней частью экрана.
    """

    position_x = 200
    position_y = 600
    image = None
    screen = None

    def __init__(self, screen, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.screen = screen
        self._load_image()
        self._spawn()

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

    def input(self):
        ...

    def draw(self):
        # Отрисовка корабля игрока на экране
        self.screen.blit(self.image, self.position_x, self.position_y)

    def _spawn(self):
        self.position_y = 600
        self.position_x = 200