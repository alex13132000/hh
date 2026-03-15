import pygame




class Button:
    def __init__ (self, scene, text, x, y, width, height, on_click):
        self.scene = scene
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(self.scene.screen, 'black', self.rect)

    def on_click(self):
        ...