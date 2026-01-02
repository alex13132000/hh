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
    speed = 5

    def __init__(self, screen, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.screen = screen
        self._load_image()
        self._spawn()

    def input(self):
        ...

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
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.position_x -= self.speed
        if keys[pygame.K_d]:
            self.position_x += self.speed
        if keys[pygame.K_w]:
            self.position_y -= self.speed
        if keys[pygame.K_s]:
            self.position_y += self.speed

        if self.position_x < 16:
            self.position_x = 16
        if self.position_x > 368:
            self.position_x = 368

        if self.position_y < 300:
            self.position_y = 300
        if self.position_y > 684:
            self.position_y = 684

    def _spawn(self):
        self.position_y = 600
        self.position_x = 200