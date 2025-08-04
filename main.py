import pygame
import random

pygame.init()

# initialize screen
WIDTH, HEIGHT = 600, 500
BALL_SPEED = 7
PADDLE_SPEED = 7
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# colors
BACKGROUND_COLOR = (15, 23, 42)
BALL_COLOR = (0, 255, 255)
PADDLE_COLOR = (168, 85, 247)
TEXT_COLOR = (241, 245, 249)
MIDLINE_COLOR = (100, 116, 139)

# game state
score1 = 0
score2 = 0
player1_name = "A"
player2_name = "B"

ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
paddle1 = pygame.Rect(50, HEIGHT // 2 - 60, 10, 120)
paddle2 = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 60, 10, 120)

ball_dx = BALL_SPEED * random.choice((1, -1))
ball_dy = BALL_SPEED * random.choice((1, -1))
paddle1_dy = 0
paddle2_dy = 0
ball_in_motion = True

# draw scores
def draw_scores():
    font = pygame.font.Font(None, 36)
    score1_text = font.render(f"{player1_name}: {score1}", True, TEXT_COLOR)
    score2_text = font.render(f"{player2_name}: {score2}", True, TEXT_COLOR)
    screen.blit(score1_text, (10, 10))
    screen.blit(score2_text, (WIDTH - score2_text.get_width() - 10, 10))

# check collision
def check_collision(ball, paddle):
    return ball.colliderect(paddle)

# reset ball
def reset_ball_position():
    side = random.choice(('left', 'right'))
    if side == 'left':
        ball.x = 50 + 20
        ball_dx = BALL_SPEED
    else:
        ball.x = WIDTH - 50 - 30 - 10
        ball_dx = -BALL_SPEED
    ball.y = HEIGHT // 2 - 15
    return ball_dx

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle2_dy = -PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                paddle2_dy = PADDLE_SPEED
            elif event.key == pygame.K_SPACE:
                ball_in_motion = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddle2_dy = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_dy = -PADDLE_SPEED
    elif keys[pygame.K_s]:
        paddle1_dy = PADDLE_SPEED
    else:
        paddle1_dy = 0

    # update ball
    if ball_in_motion:
        ball.x += ball_dx
        ball.y += ball_dy

    # bounce on top/bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    # collision with paddles
    if check_collision(ball, paddle1) or check_collision(ball, paddle2):
        ball_dx *= -1

    # scoring
    if ball.left <= 0:
        score2 += 1
        if score2 == 5:
            running = False
        else:
            ball_dx = reset_ball_position()
            ball_in_motion = False
    elif ball.right >= WIDTH:
        score1 += 1
        if score1 == 5:
            running = False
        else:
            ball_dx = reset_ball_position()
            ball_in_motion = False

    # update paddles
    paddle1.y += paddle1_dy
    paddle2.y += paddle2_dy
    paddle1.y = max(0, min(HEIGHT - paddle1.height, paddle1.y))
    paddle2.y = max(0, min(HEIGHT - paddle2.height, paddle2.y))

    # draw everything
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, PADDLE_COLOR, paddle1)
    pygame.draw.rect(screen, PADDLE_COLOR, paddle2)
    pygame.draw.ellipse(screen, BALL_COLOR, ball)
    pygame.draw.line(screen, MIDLINE_COLOR, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 3)

    draw_scores()
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
