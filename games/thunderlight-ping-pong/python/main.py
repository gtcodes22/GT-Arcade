import pygame, sys, random

pygame.init()

# ----------
# CONSTANTS
# ----------

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800

# Cap the frame rate so the game speed doesn't depend on the computer
FPS = 60

PLAYER_NAME = "Player"
CPU_NAME = "CPU"
CPU_LABEL_X = SCREEN_WIDTH/4
PLAYER_LABEL_X = 3 * SCREEN_WIDTH/4
LABEL_Y_OFFSET = 5

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100

BALL_WIDTH = 30
BALL_HEIGHT = 30

# The ball spawns from a random height near the top of the screen
BALL_MIN_POSITION_Y, BALL_MAX_POSITION_Y = 10, 100

CPU_MAX_SPEED = 4  # 3 was too easy; 4 feels balanced
PLAYER_MAX_SPEED = 6

# ----------
# DEFINITIONS
# ----------

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Pong Game!")

clock = pygame.time.Clock()

# Text: fonts, and the labels that never change
name_font = pygame.font.Font(None, 50)
score_font = pygame.font.Font(None, 100)

cpu_name_surface = name_font.render(CPU_NAME, True, "white")
player_name_surface = name_font.render(PLAYER_NAME, True, "white")

cpu_name_rect = cpu_name_surface.get_rect(midtop=(CPU_LABEL_X, LABEL_Y_OFFSET))
player_name_rect = player_name_surface.get_rect(midtop=(PLAYER_LABEL_X, LABEL_Y_OFFSET))

# CPU paddle: left edge, vertically centred
cpu = pygame.Rect(0, 0, PADDLE_WIDTH, PADDLE_HEIGHT)
cpu.centery = SCREEN_HEIGHT/2

# Player paddle: right edge, vertically centred
player = pygame.Rect(0, 0, PADDLE_WIDTH, PADDLE_HEIGHT)
player.midright = (SCREEN_WIDTH, SCREEN_HEIGHT/2)

ball = pygame.Rect(0, 0, BALL_WIDTH, BALL_HEIGHT)
ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

# ----------
# VARIABLES
# ----------

player_speed = 0
cpu_speed = 0
ball_speed_x = 6
ball_speed_y = 6

cpu_points, player_points = 0, 0

# ----------
# FUNCTIONS
# ----------

def reset_ball():
    global ball_speed_x, ball_speed_y

    # Serve from the middle of the screen at a random height
    ball.x = SCREEN_WIDTH/2 - BALL_WIDTH/2
    ball.y = random.randint(BALL_MIN_POSITION_Y, BALL_MAX_POSITION_Y)

    # Random direction on each axis
    ball_speed_x *= random.choice([-1, 1])
    ball_speed_y *= random.choice([-1, 1])

def point_won(winner):
    global cpu_points, player_points

    if winner == "cpu":
        cpu_points += 1
    if winner == "player":
        player_points += 1

    reset_ball()

def animate_ball():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Bounce off the top and bottom edges
    if ball.bottom >= SCREEN_HEIGHT or ball.top <= 0:
        ball_speed_y *= -1

    # Bounce off the paddles
    if ball.colliderect(player) or ball.colliderect(cpu):
        ball_speed_x *= -1

    # Past a paddle: the other side scores
    if ball.right >= SCREEN_WIDTH:
        point_won("cpu")

    if ball.left <= 0:
        point_won("player")

def keep_paddle_on_screen(paddle_rect):
    if paddle_rect.top <= 0:
        paddle_rect.top = 0
    if paddle_rect.bottom >= SCREEN_HEIGHT:
        paddle_rect.bottom = SCREEN_HEIGHT

def animate_player():
    player.y += player_speed
    keep_paddle_on_screen(player)

def animate_cpu():
    global cpu_speed
    cpu.y += cpu_speed

    keep_paddle_on_screen(cpu)

    # Make computer paddle follow the ball's vertical centre
    if ball.centery <= cpu.centery:
        cpu_speed = -CPU_MAX_SPEED
    if ball.centery >= cpu.centery:
        cpu_speed = CPU_MAX_SPEED

# ----------
# GAME LOOP
# ----------

while True:
    # Check for events (like closing the window, pressing keys)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # In pygame y grows downward, so up is negative
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -PLAYER_MAX_SPEED
            elif event.key == pygame.K_DOWN:
                player_speed = PLAYER_MAX_SPEED

        # Stop moving when the key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_speed = 0

    # Change the positions of the game objects
    animate_ball()
    animate_player()
    animate_cpu()

    # Clear the screen with each frame
    screen.fill('black')

    # Build the score images, then draw the names and scores
    cpu_score_surface = score_font.render(str(cpu_points), True, "white")
    player_score_surface = score_font.render(str(player_points), True, "white")

    cpu_score_rect = cpu_score_surface.get_rect(midtop=(CPU_LABEL_X, cpu_name_rect.bottom))
    player_score_rect = player_score_surface.get_rect(midtop=(PLAYER_LABEL_X, player_name_rect.bottom))

    screen.blit(cpu_name_surface, cpu_name_rect)
    screen.blit(cpu_score_surface, cpu_score_rect)
    screen.blit(player_name_surface, player_name_rect)
    screen.blit(player_score_surface, player_score_rect)

    # Draw game objects. Order matters: later items appear on top
    pygame.draw.aaline(screen, 'white', (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))
    pygame.draw.ellipse(screen, 'white', ball)
    pygame.draw.rect(screen, 'white', cpu)
    pygame.draw.rect(screen, 'white', player)

    pygame.display.update()

    clock.tick(FPS)

