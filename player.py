import pygame

import scene


IMG = 'assets/images/player_ship/player.png'
SPAWN = [200, 600]
SPEED = 5
SHOT_DELAY = 30
SHOT_MP3 = 'assets/musics/shot.mp3'

class Player:
    def __init__(self, scene):
        self.last_shot = SHOT_DELAY
        self.scene = scene
        self._spawn()
        self.image = pygame.image.load(IMG)  # TODO: рассчитать середину player_zone для начальной позиции
        self.shot_mp3 = pygame.mixer.Sound(SHOT_MP3)
        self.rect = self.image.get_rect(topleft=(self.position_x, self.position_y))

    def _move(self, SPEED, axis='x'):
        # TODO использовать self.rect scene.player_zone для ограничения движения
        saved_rect = self.rect
        
        if axis == 'x':
            self.rect += SPEED
        elif axis == 'y':
            self.rect += SPEED

        # Ограничение зоны движения
        if not self.scene.player_zone.contains(self.rect):
            self.rect = saved_rect

    def _shoot(self):
        if self.last_shot > SHOT_DELAY:
            self.scene.shoot()
            self.last_shot = 0
            self.shot_mp3.play()

    def update(self):
        self.last_shot += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self._move(-SPEED, 'x')
        if keys[pygame.K_d]:
            self._move(SPEED, 'x')
        if keys[pygame.K_w]:
            self._move(-SPEED, 'y')
        if keys[pygame.K_s]:
            self._move(SPEED, 'y')
        if keys[pygame.K_SPACE]:
            self._shoot()

    def draw(self):
        # Отрисовка корабля игрока на экране
        self.scene.screen.blit(
            source=self.image,
            dest=(self.position_x, self.position_y),
        )

    def _spawn(self):
        self.position_y = 600
        self.position_x = 200

