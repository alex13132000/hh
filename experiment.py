import pygame

pygame.init()

SIZE = 1000, 1000
FPS = 20


clock = pygame.time.Clock()

screen = pygame.display.set_mode(SIZE)

while True:
    clock.tick(FPS)





'''
    {
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
    },
'''

