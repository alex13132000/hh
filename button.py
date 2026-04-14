import pygame




class Button:
    def __init__ (self, scene, text, x, y, width, height, action=None):
        self.scene = scene
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont('serif', 50)
        self.action = action
        self.label = self.font.render(
            self.text,
            True,
            pygame.Color('white'),
        )

    def draw(self):
        pygame.draw.rect(self.scene.screen, 'black', self.rect)
        text_rect = self.label.get_rect(center=self.rect.center)
        self.scene.screen.blit(source=self.label, dest=text_rect)

    def is_clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN and
            event.button == 1 and
            self.rect.collidepoint(event.pos)
        )
    


    def on_click(self):
        if self.action:
            self.action()
        print(self.text)