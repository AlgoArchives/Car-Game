import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Load car image
car_image = pygame.image.load("car.png")
car_image = pygame.transform.scale(car_image, (60, 30))  # Scale the car image

# Game variables
car_x, car_y = WIDTH // 2, HEIGHT // 2
car_angle = 0
car_speed = 0
max_speed = 10
acceleration = 0.1
deceleration = 0.05
turn_speed = 5

# Draw the car
def draw_car(x, y, angle):
    rotated_car = pygame.transform.rotate(car_image, angle)
    new_rect = rotated_car.get_rect(center=car_image.get_rect(topleft=(x, y)).center)
    screen.blit(rotated_car, new_rect.topleft)

# Main game loop
running = True
while running:
    screen.fill(GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        car_speed = min(car_speed + acceleration, max_speed)
    elif keys[pygame.K_DOWN]:
        car_speed = max(car_speed - deceleration, -max_speed)
    else:
        if car_speed > 0:
            car_speed = max(car_speed - deceleration, 0)
        elif car_speed < 0:
            car_speed = min(car_speed + deceleration, 0)
    
    if keys[pygame.K_LEFT]:
        car_angle += turn_speed if car_speed != 0 else 0
    if keys[pygame.K_RIGHT]:
        car_angle -= turn_speed if car_speed != 0 else 0

    car_x += car_speed * math.sin(math.radians(car_angle))
    car_y -= car_speed * math.cos(math.radians(car_angle))

    draw_car(car_x, car_y, car_angle)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()