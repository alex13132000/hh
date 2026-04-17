import time
import pygame

import background
import bullet
import button
import enemy
import hearts
import player
import score


WIDTH, HEIGHT = 420, 720
FPS = 60
ENEMY_DELAY = 1.5
BG_MUSIC = 'assets/musics/music_BG.mp3'
PLAYER_ZONE = 16, 360, 388, 344
SCORE_ZONE = 210, 5, 200, 50


class Scene:
    def __init__(self):
        pygame.init()
        pygame.mixer.music.load(BG_MUSIC)
        pygame.mixer.music.play(loops=-1)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self._background = background.Background(self)
        self._clock = pygame.time.Clock()
        self._transients = []
        self.hearts = hearts.Hearts(self)
        self.player = player.Player(self, PLAYER_ZONE)
        self.score = score.Score(self, SCORE_ZONE)
        self.state = 'MENU'
        self.last_enemy_timestamp = time.monotonic()
        self.last_bullet_timestamp = time.monotonic()
        self.reset_game()
        self.play_button = button.Button(
            self,
            'play',
            110, 200, 200, 60, self.action_play
            )
        self.restart_button = button.Button(
            self,
            'restart',
            110, 300, 200, 60, self.action_restart
            )
        self.exit_button = button.Button(
            self,
            'exit',
            110, 400, 200, 60
            )

    def action_play(self):
        self.state = 'PLAY'

    def action_restart(self):
        self.reset_game()
        self.state = 'PLAY'

    def action_exit(self):
        pygame.quit()

    def _add_enemy(self):
        now = time.monotonic()
        if now - self.last_enemy_timestamp >= ENEMY_DELAY:
            self._transients.append(enemy.Enemy(self))
            self.last_enemy_timestamp = now

    def shoot(self):
        now = time.monotonic()
        if now - self.last_bullet_timestamp >= player.SHOT_DELAY:
            self._transients.append(bullet.Bullet(self, *self.player.rect.midtop))
            self.last_bullet_timestamp = now
            self.player.shot_mp3.play()

    def get_bullets(self):
        return [o for o in self._transients if isinstance(o, bullet.Bullet)]

    def remove_transient(self, transient):
        self._transients.remove(transient)

    def reset_game(self):
        self._background = background.Background(self)
        self._transients = []
        self.hearts = hearts.Hearts(self)
        self.player = player.Player(self, PLAYER_ZONE)
        self.score = score.Score(self, SCORE_ZONE)
        self.last_enemy_timestamp = time.monotonic()
        self.last_bullet_timestamp = time.monotonic()

    def update(self):
        self._background.update()
        self.player.update()
        for b in self._transients:
            b.update()
        self._add_enemy()

    def draw(self):
        self._background.draw()
        self.player.draw()
        for b in self._transients:
            b.draw()
        self.score.draw()
        self.hearts.draw()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.action_exit()

                if self.state == 'MENU':
                    if self.play_button.is_clicked(event):
                        self.play_button.on_click()
                    if self.exit_button.is_clicked(event):
                        self.exit_button.on_click()

                elif self.state == 'GAME_OVER':
                    if self.restart_button.is_clicked(event):
                        self.restart_button.on_click()
                    if self.exit_button.is_clicked(event):
                        self.exit_button.on_click()

            if self.state == 'PLAY':
                self.update()
                self.draw()

            elif self.state == 'MENU':
                self.screen.fill('blue')
                self.play_button.draw()
                self.exit_button.draw()

            elif self.state == 'GAME_OVER':
                self.screen.fill('black')
                self.restart_button.draw()
                self.exit_button.draw()

            pygame.display.flip()
            self._clock.tick(FPS)