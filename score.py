import pygame


class Score:
    def __init__(self, scene, zone):
        self.scene = scene
        self.zone = zone
        self.score = 0
        self.font = pygame.font.SysFont('serif', 50)

    def draw(self):
        score = self.font.render(
            str(self.score),
            True,
            pygame.Color('white'),
        )

        self.scene.screen.blit(source=score, dest=self.zone)