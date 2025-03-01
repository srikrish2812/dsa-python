import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Bouncing in a Spinning Hexagon")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BALL_COLOR = (255, 100, 100)

# Ball properties
ball_radius = 15
ball_pos = pygame.math.Vector2(WIDTH / 2, HEIGHT / 2)
ball_vel = pygame.math.Vector2(4, -2)

# Physics properties
gravity = pygame.math.Vector2(0, 0.2)
friction = 0.99

# Hexagon properties
hexagon_center = pygame.math.Vector2(WIDTH / 2, HEIGHT / 2)
hexagon_radius = 300
hexagon_sides = 6
hexagon_angle = 0
hexagon_rotation_speed = 0.01

clock = pygame.time.Clock()

def get_hexagon_points(center, radius, sides, angle_offset):
    points = []
    for i in range(sides):
        angle = 2 * math.pi * i / sides + angle_offset
        x = center.x + radius * math.cos(angle)
        y = center.y + radius * math.sin(angle)
        points.append((x, y))
    return points

def reflect_velocity(velocity, normal):
    return velocity - 2 * velocity.dot(normal) * normal

def check_collision(ball_pos, ball_radius, points):
    collision = False
    normal = pygame.math.Vector2(0, 0)
    for i in range(len(points)):
        p1 = pygame.math.Vector2(points[i])
        p2 = pygame.math.Vector2(points[(i + 1) % len(points)])
        edge = p2 - p1
        edge_normal = pygame.math.Vector2(-edge.y, edge.x).normalize()
        ball_to_edge = ball_pos - p1
        distance = ball_to_edge.dot(edge_normal)
        projection = ball_to_edge.dot(edge.normalize())
        if 0 <= projection <= edge.length() and distance <= ball_radius:
            collision = True
            normal = edge_normal
            break
    return collision, normal

# Main loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update hexagon rotation
    hexagon_angle += hexagon_rotation_speed

    # Update ball physics
    ball_vel += gravity
    ball_pos += ball_vel
    ball_vel *= friction

    # Get hexagon points
    hexagon_points = get_hexagon_points(hexagon_center, hexagon_radius, hexagon_sides, hexagon_angle)

    # Check collision and reflect velocity
    collision, normal = check_collision(ball_pos, ball_radius, hexagon_points)
    if collision:
        ball_vel = reflect_velocity(ball_vel, normal)
        ball_pos += normal * (ball_radius - (ball_pos - hexagon_center).length() + hexagon_radius)

    # Clear screen
    screen.fill(BLACK)

    # Draw hexagon
    pygame.draw.polygon(screen, WHITE, hexagon_points, 3)

    # Draw ball
    pygame.draw.circle(screen, BALL_COLOR, (int(ball_pos.x), int(ball_pos.y)), ball_radius)

    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()