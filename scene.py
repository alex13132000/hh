import random
import sys
import time

import pygame

import background
import bonus
import bullet
import button
from enemy import SCurveRaiderI as scr1
from enemy import SCurveTankI as sct1
from enemy import SCurveSpeedI as scs1
import hearts
import player
import score


WIDTH, HEIGHT = 420, 720
FPS = 60
BONUS_DELAY = 1
ENEMY_DELAY = 1.5
BG_MUSIC = 'assets/musics/music_BG.mp3'
PLAYER_ZONE = 16, 360, 388, 344
SCORE_ZONE = 210, 5, 200, 50


class Scene:
    def __init__(self):
        pygame.init()
        pygame.mixer.music.load(BG_MUSIC)
        # pygame.mixer.music.play(loops=-1)
        self.spawn_patterns = (
            (scr1, scr1, scr1, scr1, sct1, scs1, sct1, scs1),
            (scs1, scs1, scs1, sct1, sct1, scr1, scr1, scs1),
            (sct1, sct1, sct1, scr1, scr1, scs1, scs1, scr1),
        )
        self.game_over_font = pygame.font.SysFont('serif', 50)
        self.over_banner = self.game_over_font.render(
            'GAME OVER',
            True,
            'white',
        )
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
        if hasattr(self, 'hearts') and self.hearts.hp > 0:
            self.is_playing = True

    def action_restart(self):
        self.reset_game()
        self.is_playing = True

    def action_exit(self):
        pygame.quit()
        sys.exit()

    def _add_enemy(self):
        now = time.monotonic()  # TODO: get_ticks
        if now - self.last_enemy_timestamp >= ENEMY_DELAY:
            while ...:
                try:
                    next_enemy = next(enemy_it)(self)
                    break
                except (StopIteration, NameError):
                    enemy_it = iter(random.choice(self.spawn_patterns))
            self.transients.append(next_enemy)
            self.last_enemy_timestamp = now

    def add_bonus(self):
        now = time.monotonic()
        if now - self.last_bonus_timestamp >= BONUS_DELAY:
            if random.random() < 0.5:
                random.choice([bonus.BonusBomb, bonus.BonusBullet, bonus.BonusHealth])(self)
                self.last_bonus_timestamp = now

    def get_bullets(self):
        return [o for o in self.transients if isinstance(o, bullet.Bullet)]

    def reset_game(self):
        self._background = background.Background(self)
        self.transients = []
        self.hearts = hearts.Hearts(self)
        self.player = player.Player(self, PLAYER_ZONE)
        self.score = score.Score(self, SCORE_ZONE)
        self.last_enemy_timestamp = time.monotonic()
        self.last_bullet_timestamp = time.monotonic()
        self.last_bonus_timestamp = time.monotonic()

    def update(self):
        self._background.update()
        self.player.update()
        self._add_enemy()
        self.add_bonus()
        for b in self.transients:
            b.update()

    def draw(self):
        self._background.draw()
        self.player.draw()
        for b in self.transients:
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
                if self.hearts.hp > 0:
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