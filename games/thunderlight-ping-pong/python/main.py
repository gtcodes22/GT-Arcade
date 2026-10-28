import pygame, sys

# FUNCTIONS

def animate_ball():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Collision detection
    # Change the ball's direction by reversing its speed
    if ball.bottom >= screen_height or ball.top <= 0:
        ball_speed_y *= -1 
    if ball.right >= screen_width or ball.left <= 0:
        ball_speed_x *= -1

    # Check for collision with the paddles
    if ball.colliderect(player) or ball.colliderect(cpu):
        ball_speed_x *= -1

def animate_player():
    player.y += player_speed
    
    # Keep the player paddle within the screen's boundaries
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def animate_cpu():
    global cpu_speed
    cpu.y += cpu_speed

    # Make computer paddle follow the centre of the ball
    if ball.centery <= cpu.centery:
        cpu_speed = -6
    if ball.centery >= cpu.centery:
        cpu_speed = 6

    # Keep the computer paddle within the screen's boundaries
    if cpu.top <= 0:
        cpu.top = 0
    if cpu.bottom >= screen_height:
        cpu.bottom = screen_height

# Initialize Pygame
pygame.init()

# DEFINITIONS

screen_width = 1280
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pong Game!") # The title of the window

clock = pygame.time.Clock() # Controls the game's frame rate

# Create a rectangle with 30x30 pixels with origin at the screen's top left corner.
ball = pygame.Rect(0, 0, 30, 30) 
ball.center = (screen_width/2, screen_height/2) # Place the ball in the centre of the screen.

# Create the two paddles

# CPU paddle is centred vertically on the left side of the screen
cpu = pygame.Rect(0, 0, 20, 100)
cpu.centery = screen_height/2

# Player paddle is centred vertically on the right side of the screen
player = pygame.Rect(0, 0, 20, 100)
player.midright = (screen_width, screen_height/2)

# Animation

ball_speed_x = 6
ball_speed_y = 6
player_speed = 0
cpu_speed = 6

# GAME LOOP

while True:
    # Check for events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # move paddle up/down by decreasing/increasing the y coordinate
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -6 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed = 6
        
        # set the paddle speed to 0 when the key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed = 0

    # Change the positions of the game objects
    animate_ball()
    animate_player()
    animate_cpu()
    
    # Clear the screen with each frame (fill it with black)
    screen.fill('black')

    # Draw the game objects
    pygame.draw.aaline(screen, 'white', (screen_width/2, 0), (screen_width/2, screen_height))
    pygame.draw.ellipse(screen, 'white', ball)
    pygame.draw.rect(screen, 'white', cpu)
    pygame.draw.rect(screen, 'white', player)

    # Update the display
    pygame.display.update()
    clock.tick(60) # Limit the frame rate to 60 fps (or else the computer chooses the highest frame rate possible, which is usually too fast for a game)

