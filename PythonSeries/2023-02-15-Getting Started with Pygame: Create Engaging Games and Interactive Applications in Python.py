# One of the most popular Python libraries for creating games and other interactive applications is Pygame.
# To get started with Pygame, we first need to install it. 
# This can be done using pip: 
#pip install pygame > In terminal

# Once we have Pygame installed, we can start writing our first game. 
# Here is a simple example of a Pygame program that creates a window and displays a moving rectangle:
import pygame

# Initialize Pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("My First Pygame Program")

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw a rectangle
    pygame.draw.rect(screen, (255, 0, 0), (20, 20, 60, 40))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()