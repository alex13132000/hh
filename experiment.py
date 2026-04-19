import pygame

ENEMY_DATA = {
      "id": 1,
      "name": "Spiral Diver I",
      "tier": 1,
      "entry_path": {
        "type": "bezier",
        "control_points": [
          { "x": -0.2, "y": 1.1 },
          { "x": 0.1, "y": 0.8 },
          { "x": 0.3, "y": 0.5 },
          { "x": 0.5, "y": 0.2 }
        ]
      },
      "attack_path": {
        "type": "bezier",
        "control_points": [
          { "x": 0.5, "y": 0.2 },
          { "x": 0.45, "y": 0.4 },
          { "x": 0.5, "y": 0.7 },
          { "x": 0.5, "y": 1.1 }
        ]
      },
      "exit_path": {
        "type": "bezier",
        "control_points": [
          { "x": 0.5, "y": 1.1 },
          { "x": 0.7, "y": 1.2 },
          { "x": 1.1, "y": 1.0 }
        ]
      }
    }

class Enemy:
    def __init__(self, data):
        self.paths = [[(p["x"] * 1000, p["y"] * 1000) for p in data[k]["control_points"]] for k in data]
        self.phase, self.t = 0, 0.0

    def update_and_draw(self, surface):
        if self.phase >= len(self.paths): return
        p, t = self.paths[self.phase], self.t
        
        if len(p) == 3:
            xy = [(1-t)**2 * p[0][i] + 2*(1-t)*t * p[1][i] + t**2 * p[2][i] for i in (0, 1)]
        else:
            xy = [(1-t)**3 * p[0][i] + 3*(1-t)**2*t * p[1][i] + 3*(1-t)*t**2 * p[2][i] + t**3 * p[3][i] for i in (0, 1)]
            
        pygame.draw.circle(surface, (255, 50, 50), (int(xy[0]), int(xy[1])), 15)
        
        self.t += 0.015
        if self.t >= 1: 
            self.t, self.phase = 0.0, self.phase + 1

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
enemy = Enemy(ENEMY_DATA)

while True:
    if pygame.event.get(pygame.QUIT): exit()
    screen.fill((10, 10, 20))
    
    enemy.update_and_draw(screen)
    
    pygame.display.flip()
    clock.tick(60)