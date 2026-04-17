import time
import pygame
import sys

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
        self.game_over_font = pygame.font.SysFont('serif', 50)
        self.over_banner = self.game_over_font.render('GAME OVER', True, 'white')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self._clock = pygame.time.Clock()
        self.reset_game()
        self.is_playing = False
        self.menu_buttons = [
            button.Button(
                self, 'Resume', 110, 200, 200, 60, self.action_resume),
            button.Button(
                self, 'Restart', 110, 300, 200, 60, self.action_restart),
            button.Button(
                self, 'Exit', 110, 400, 200, 60, self.action_exit),
        ]

    def action_resume(self):
        self.is_playing = True

    def action_restart(self):
        self.reset_game()
        self.is_playing = True

    def action_exit(self):
        pygame.quit()
        sys.exit()

    def _add_enemy(self):
        now = time.monotonic()
        if now - self.last_enemy_timestamp >= self.enemy_delay:
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
        if transient in self._transients:
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

    def handle_menu_events(self, event):
        for b in self.menu_buttons:
            if b.is_clicked(event):
                b.on_click()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.action_exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.is_playing = not self.is_playing
                if not self.is_playing:
                    self.handle_menu_events(event)

            if self.is_playing:
                self.update()
                self.draw()
                if self.hearts.hp <= 0:
                    self.screen.blit(self.over_banner, (110, 300, 200, 60))
            else:
                self.screen.fill('blue')
                for b in self.menu_buttons:
                    b.draw()


            pygame.display.flip()
            self._clock.tick(FPS)