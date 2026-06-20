import pygame


IMG = 'assets/images/boss_ship/boss.png'


class Player:
    def __init__(self, scene):
        self.scene = scene
        self.image = pygame.image.load(IMG)
        self.rect = self.image.get_rect()

    def draw(self):
        ...

    def update(self):
        ...
    
