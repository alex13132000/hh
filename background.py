import pygame


IMG = 'assets/images/BG/BG_1.png'
SPEED = 2


class Background:
    def __init__(self, scene):
        self.scene = scene
        self.y = 0
        image = pygame.image.load(IMG)
        image_size = image.get_size()
        self.height = image_size[1] * 2
        self.bg = pygame.Surface((image_size[0], self.height))
        self.bg.blit(source=image, dest=(0, 0))
        self.bg.blit(
            source=pygame.transform.flip(
                surface=image,
                flip_x=False,
                flip_y=True,
            ),
            dest=(0, image_size[1]),
        )

    def update(self):
        self.y += SPEED
        if self.y >= self.height:
            self.y = 0

    def draw(self):
        self.scene.screen.blit(source=self.bg, dest=(0, self.y))
        self.scene.screen.blit(source=self.bg, dest=(0, self.y - self.height))