import sys

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

WIDTH, HEIGHT = 1000, 1000
FPS = 60  # frames per second
SPEED = 100  # enemy speed pixels per second


def get_pos(rel_coord):
    rel_coord = list(rel_coord)
    return rel_coord[0] * WIDTH, rel_coord[1] * HEIGHT

def bezier_point(p0, p1, p2, p3, t):
    """Return a point on a cubic Bezier curve at parameter t."""
    u = 1 - t
    return (
        u**3 * p0[0] + 3*u**2*t * p1[0] + 3*u*t**2 * p2[0] + t**3 * p3[0],
        u**3 * p0[1] + 3*u**2*t * p1[1] + 3*u*t**2 * p2[1] + t**3 * p3[1]
    )

# bezier_point(, p1, p2, p3, t)

position_0 = get_pos(
    ENEMY_DATA['entry_path']['control_points'][0].values(),
)

position_1 = get_pos(
    ENEMY_DATA['entry_path']['control_points'][1].values(),
)


position_2 = get_pos(
    ENEMY_DATA['entry_path']['control_points'][2].values(),
)


position_3 = get_pos(
    ENEMY_DATA['entry_path']['control_points'][3].values(),
)



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((10, 10, 20))

    pygame.draw.circle(screen, (20, 20, 20), position, 20)
    pygame.display.flip()
    clock.tick(FPS)