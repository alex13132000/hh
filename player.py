"""Модуль класса Player.
"""

import pygame


SHIP_IMAGE_FILE = 'assets/images/player_ship.png'

class Player:
    """Корабль игрока.
        - Класс спрайта с позицией, движением (влево/вправо) и стрельбой.
        - Ограничение движения нижней частью экрана.
    """

    position = None
    image = None

    def __init__(self):
        self._load_image()

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