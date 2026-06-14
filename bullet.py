import pygame


IMG = 'assets/images/player_ship/bullet_P.png'
SPEED = 10
BOUNDARY = -20


class Bullet:
    def __init__(self, scene, pos):
        self.scene = scene
        self.image = pygame.image.load(IMG)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.scene.transients.append(self)

    def update(self):
        self.rect.y -= SPEED
        if self.rect.y < BOUNDARY:
            self.scene.transients.remove(self)

    def draw(self):
        self.scene.screen.blit(source=self.image, dest=self.rect)



