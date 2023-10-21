import pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image Display Example")

# Load the image
image_path = "wp12396509-cyberpunk-edgerunners-4k-wallpapers.jpg"  # Replace with the actual image path
image = pygame.image.load(image_path)

# Get the rect of the image and position it
image_rect = image.get_rect()
image_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the image onto the screen
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.flip()

pygame.quit()

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game UI Example")

# Colors
WHITE = (255, 255, 255)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill(WHITE)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
