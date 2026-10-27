import pygame, sys

pygame.init()

# DEFINITIONS

screen_width = 1280
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pong Game!") # The title of the window

clock = pygame.time.Clock() # Controls the game's frame rate

# GAME LOOP

while True:
    # Check for events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the display
    pygame.display.update()
    clock.tick(60) # Limit the frame rate to 60 fps (or else the computer chooses the highest frame rate possible, which is usually too fast for a game)