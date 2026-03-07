import pygame


IMG = 'assets/images/player_ship/bullet_P.png'
SPEED = 10
BOUNDARY = -20

# Rect(object) -> Rect

class Bullet:
    def __init__(self, scene, position_x, position_y):
        self.scene = scene
        self.image = pygame.image.load(IMG)
        self.rect = self.image.get_rect()
        self.rect.x = position_x
        self.rect.y = position_y

    def update(self):
        self.rect.y -= SPEED
        if self.rect.y < BOUNDARY:
            self.scene.remove_transient(self)

    def draw(self):
        self.scene.screen.blit(source=self.image, dest=self.rect)
