import pygame

IMAGE = 'assets/images/player_ship/bullet_P.png'
SPEED = 10


class Bullet:
    def __init__(self, position_x, position_y, screen):
        self.screen = screen
        self.position_x = position_x
        self.position_y = position_y
        self.image = pygame.image.load(IMAGE)

    def update(self):
        if self.position_y > -20:
            self.position_y -= SPEED

    def draw(self):
        self.screen.blit(
            source=self.image,
            dest=(self.position_x, self.position_y),
        )
