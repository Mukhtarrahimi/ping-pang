import pygame
import random

# initailize board
pygame.init()
WIDHT, HEIGHT = 600, 500
BALL_SPEED = 7
PADDLE_SPEDD = 7

# color
BACKGROUND_COLOR = (15, 23, 42)     
BALL_COLOR = (0, 255, 255)          
PADDLE_COLOR = (168, 85, 247)      
TEXT_COLOR = (241, 245, 249)        
MIDLINE_COLOR = (100, 116, 139)    

# initialize players Required
score1 = 0
score2 = 0
player1_name = "A"
player2_name = "B"
ball = pygame.rect(WIDHT // 2 - 15, HEIGHT // 2 - 15, 30, 30)
paddle1 = pygame.Rect(50, HEIGHT //2 - 60, 10, 120)
paddle2 = pygame.Rect(WIDHT - 60, HEIGHT // 2 - 60 , 10, 120)
ball_dx = BALL_SPEED * random.choice((1, -1))
ball_dy = BALL_SPEED * random.choice((1, -1))
paddle1_dy = 0
paddle2_dy = 0
ball_in_motion = True

# function for draw score
def draw_scores():
    font = pygame.font.Font(None, 36)
    score1_text = font.render(f"{player1_name}: {score1}", True, TEXT_COLOR)
    score2_text = font.render(f"{player2_name}: {score2}", True, TEXT_COLOR)
    screen.blit(score1_text, (10, 10))
    screen.blit(score2_text), (WIDHT - score2_text.get_width() - 10, 10)
    
