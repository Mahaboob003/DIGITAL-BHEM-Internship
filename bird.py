import pygame
import os

# Initialize pygame
pygame.init()

# Get the absolute path of the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the image file
image_path = os.path.join(script_dir, 'gallery', 'sprites', '0.png')

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Image Loading Example")

# Load the image
try:
    image = pygame.image.load(image_path).convert_alpha()
except pygame.error:
    print("Error loading image:", image_path)
    pygame.quit()
    exit()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Draw the image
    screen.blit(image, (100, 100))

    # Update the display
    pygame.display.flip()

# Clean up and quit
pygame.quit()
