import pygame


IMG = 'assets/images/enemy_ship/blast.png'
LIFE_TIME = 500

class Blast:
    def __init__(self, scene, position):
        self.image = pygame.image.load(IMG)
        self.scene = scene
        self.position = position
        self.spawn_time = pygame.time.get_ticks()
        self.scene.transients.append(self)


    def draw(self):
        self.scene.screen.blit(self.image, self.position)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.spawn_time > LIFE_TIME:
            self.scene.transients.remove(self)
