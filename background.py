import pygame

class Background:
    def init(self, image_path, speed=2):
        self.image = pygame.image.load(image_path)
        self.speed = speed
        self.y = 0
        self.height = self.image.get_height()

    def update(self):
        self.y += self.speed
        if self.y >= self.height:
            self.y = 0

    def draw(self, screen):
        screen.blit(self.image, (0, self.y))
        screen.blit(self.image, (0, self.y - self.height))