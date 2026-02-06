import background
import player
import bullet


class Scene:
    def __init__(self, screen):
        self.screen = screen
        self.background = background.Background(screen)
        self.player = player.Player(screen)
        self.bullets = []
        self.enemies = []
        self.enemy_bullets = []
        self.hp = []


    def update(self):
        ...

    def draw(self):
        ...

