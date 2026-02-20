import pygame

IMG = 'assets/enemy_ship/enemy_simple.png'
SPEED = 5


class Enemy:
    def __init__(self, scene):
        self.scene = scene
        self.image = pygame.image.load(IMG)
        self.position_x = 0
        self.position_y = 0




    def update(self):
        self.position_y += SPEED
        if self.position_y > self.scene.screen.get_height():
            self.scene.remove_enemy(self)

    def draw(self):
        self.scene.screen.blit(self.image, (self.position_x, self.position_y))