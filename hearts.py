import pygame


IMG = 'assets/images/player_ship/heart.png'
START_HP = 3
POSITION = 10, 10
STEP = 30


class Hearts:
    def __init__(self, scene):
        self.scene = scene
        self.image = pygame.image.load(IMG)
        self.hp = START_HP

    def draw(self):
        for pos in range(self.hp):
            self.scene.screen.blit(
                self.image,
                (POSITION[0] + STEP * pos, POSITION[1]),
            )
