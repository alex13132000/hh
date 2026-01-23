import pygame


BG_FILE = 'assets/images/BG/BG_1.png'
class Background:



    def __init__(self, image_path=BG_FILE, speed=2):
        self.speed = speed
        self.y = 0
        self.image = pygame.image.load(image_path)
        self.height = self.image.get_height()
        # self.image = pygame.image.load(image_path)
        
        flip_image = pygame.transform.flip(self.image, True, False)
        bg_size = self.image.get_size()
        bg_fin = (bg_size[0], bg_size[1] * 2)
        self.big_bg = pygame.Surface(bg_fin)
        self.big_bg.blit(self.image, (0, 0))
        self.big_bg.blit(flip_image, (0, self.height))

        #----------------------------------------------------
        # Запердолить в эту поверхность 2 фона
        #----------------------------------------------------


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