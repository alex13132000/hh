import random

import pygame

SPEED = 5
BOUNDARY = 800
SPAWN = 0, 400

class Bonus:
    def __init__(self, scene):
        if hasattr(self, 'image_filename'):
            self.image = pygame.image.load(self.image_filename)
        else:
            self.image_filename = None
            self.image = pygame.Surface((0, 0))

        self.scene = scene
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 400 - self.rect.width)
        self.rect.y = -50


    def update(self):
        self.rect.y += SPEED
        if self.rect.y > BOUNDARY:
            if self in self.scene.transients:
                self.scene.transients.remove(self)

    def draw(self):
        self.scene.screen.blit(source=self.image, dest=self.rect)    
    
class BonusBomb(Bonus):
    def __init__(self, scene):
        self.image_filename = 'assets/images/bonus_ship/bonus_bomb.png'
        
        super().__init__(scene)