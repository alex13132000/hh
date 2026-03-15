import pygame


IMG = 'assets/images/player_ship/player.png'
SPAWN = [200, 600]
SPEED = 5
SHOT_DELAY = 0.5
SHOT_MP3 = 'assets/musics/shot.mp3'


class Player:
    def __init__(self, scene, zone):
        self.last_shot = SHOT_DELAY
        self.scene = scene
        self.image = pygame.image.load(IMG)
        self.rect = self.image.get_rect()
        self.zone = pygame.Rect(*zone)
        self.rect.move_ip(*self.zone.center)
        self.shot_mp3 = pygame.mixer.Sound(SHOT_MP3)

    def _move(self, speed, axis='x'):
        if axis == 'x':
            self.rect.x += speed
        elif axis == 'y':
            self.rect.y += speed

        self.rect.clamp_ip(self.zone)


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
        self.scene.screen.blit(source=self.image, dest=self.rect)

