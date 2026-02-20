import pygame


IMG = 'assets/images/player_ship/bullet_P.png'
SPEED = 10
BOUNDARY = -20

class Bullet:
    def __init__(self, scene, position_x, position_y):
        self.scene = scene
        self.position_x = position_x
        self.position_y = position_y
        self.image = pygame.image.load(IMG)

    def update(self):
        self.position_y -= SPEED
        if self.position_y < BOUNDARY:
            self.scene.remove_bullet(self)

    def draw(self):
        self.scene.screen.blit(
            source=self.image,
            dest=(self.position_x, self.position_y),
        )
