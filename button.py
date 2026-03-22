import pygame




class Button:
    def __init__ (self, scene, text, x, y, width, height):
        self.scene = scene
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont('serif', 50)
        self.label = self.font.render(
            self.text,
            True,
            pygame.Color('white'),
        )

    def draw(self):
        pygame.draw.rect(self.scene.screen, 'black', self.rect)
        self.scene.screen.blit(source=self.label, dest=self.rect)

    def is_clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN and
            event.button == 1 and
            self.rect.collidepoint(event.pos)
        )

    def on_click(self):
        print(self.text)