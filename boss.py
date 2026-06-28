import pygame


IMG = 'assets/images/boss_ship/boss.png'
POS = 210, -300

class Boss:
    def __init__(self, scene):
        self.scene = scene
        self.image = pygame.image.load(IMG)
        self.rect = self.image.get_rect()
        self.rect.center = POS

    def draw(self):
        self.scene.screen.blit(self.image, self.rect)

    def update(self):
        if self.rect.centery < 0:
            self.rect.centery += 1

