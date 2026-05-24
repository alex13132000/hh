import sys

import pygame

# ENEMY_DATA = {
#     "id": 1,
#     "name": "Spiral Diver I",
#     "tier": 1,
#     "entry_path": {
#         "type": "bezier",
#         "control_points": [
#             { "x": -0.2, "y": 1.1 },
#             { "x": 0.1, "y": 0.8 },
#             { "x": 0.3, "y": 0.5 },
#             { "x": 0.5, "y": 0.2 }
#         ]
#     },
#     "attack_path": {
#         "type": "bezier",
#         "control_points": [
#             { "x": 0.5, "y": 0.2 },
#             { "x": 0.45, "y": 0.4 },
#             { "x": 0.5, "y": 0.7 },
#             { "x": 0.5, "y": 1.1 }
#         ]
#     },
#     "exit_path": {
#         "type": "bezier",
#         "control_points": [
#             { "x": 0.5, "y": 1.1 },
#             { "x": 0.7, "y": 1.2 },
#             { "x": 1.1, "y": 1.0 },
#             { "x": 1.1, "y": 1.0 },
#         ]
#     }
# }

ENEMY_DATA =     {
      "id": 6,
      "name": "S-Curve Raider I",
      "tier": 1,
      "entry_path": {
        "type": "bezier",
        "control_points": [
          { "x": -0.2, "y": 0.9 },
          { "x": 0.2, "y": 0.7 },
          { "x": -0.1, "y": 0.5 },
          { "x": 0.3, "y": 0.3 }
        ]
      },
      "attack_path": {
        "type": "bezier",
        "control_points": [
          { "x": 0.3, "y": 0.3 },
          { "x": 0.6, "y": 0.5 },
          { "x": 0.4, "y": 0.8 },
          { "x": 0.5, "y": 1.1 }
        ]
      },
      "exit_path": {
        "type": "bezier",
        "control_points": [
          { "x": 0.5, "y": 1.1 },
          { "x": 0.8, "y": 1.2 },
          { "x": 1.1, "y": 1.0 },
          { "x": 1.1, "y": 1.0 }
        ]
      }
    }


WIDTH, HEIGHT = 1000, 1000
FPS = 60  # frames per second
SPEED = 100  # enemy speed pixels per second


def get_abs_pos(rel_pos):
    rel_pos = list(rel_pos)
    return rel_pos[0] * WIDTH, rel_pos[1] * HEIGHT

def bezier_point(p0, p1, p2, p3, t):
    """Return a point on a cubic Bezier curve at parameter t."""
    u = 1 - t
    return (
        u**3 * p0[0] + 3*u**2*t * p1[0] + 3*u*t**2 * p2[0] + t**3 * p3[0],
        u**3 * p0[1] + 3*u**2*t * p1[1] + 3*u*t**2 * p2[1] + t**3 * p3[1]
    )



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
ttl = 2000
start = None
path = None

while True:
    if start is None:
        if path is None:
            path = 'entry_path'
        elif path == 'entry_path':
            path = 'attack_path'
        else:
            path = 'exit_path'
        start = pygame.time.get_ticks()
        positions = []
        for pos in ENEMY_DATA[path]['control_points']:
            positions.append(get_abs_pos(pos.values()))
    elapsed = (pygame.time.get_ticks() - start) / ttl
    pos = bezier_point(*positions, elapsed)
    if elapsed >= 1:
        start = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((10, 10, 20))
    pygame.draw.circle(screen, (255, 0, 0), pos,  20)
    pygame.display.flip()
    dt = clock.tick(FPS)

#перенести в энеми и словарь