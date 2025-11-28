"""Модуль класса Player.
"""

import pygame


SHIP_IMAGE_FILE = 'assets/player.png'

class Player:
    """Корабль игрока.
        - Класс спрайта с позицией, движением (влево/вправо) и стрельбой.
        - Ограничение движения нижней частью экрана.
    """

    position = None
    image = None
    screen = None

    def __init__(self, screen):
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
        self.screen.blit(self.image, self.position)

    def _spawn(self):
        ...