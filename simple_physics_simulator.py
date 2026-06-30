import pygame
import random

# Initialize Pygame
width = 800
height = 600
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Physics Sandbox")
clock = pygame.time.Clock()

# Constants
gravity = 0.4
bounce = -0.8  
radius = 20

# Lists to hold the ball properties
balls_x = []
balls_y = []
balls_vx = []
balls_vy = []

running = True
while running:
    screen.fill((20, 20, 30)) 

    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Click to spawn a new ball with a random side speed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            balls_x.append(float(mx))
            balls_y.append(float(my))
            balls_vx.append(random.uniform(-5, 5))
            balls_vy.append(0.0)

    # Physics Update
    for i in range(len(balls_x)):
        # Apply Gravity
        balls_vy[i] += gravity

        # Move Ball
        balls_x[i] += balls_vx[i]
        balls_y[i] += balls_vy[i]

        # Floor Collision
        if balls_y[i] >= height - radius:
            balls_y[i] = height - radius
            balls_vy[i] *= bounce

        # Wall Collisions (Left & Right)
        if balls_x[i] <= radius:
            
            balls_x[i] = radius
            balls_vx[i] *= bounce
        elif balls_x[i] >= width - radius:
            balls_x[i] = width - radius
            balls_vx[i] *= bounce

    # Draw Balls
    for i in range(len(balls_x)):
        pygame.draw.circle(screen, (0, 255, 150), (int(balls_x[i]), int(balls_y[i])), radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()