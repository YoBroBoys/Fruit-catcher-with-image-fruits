import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fruit Catcher")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
# Basket dimensions and initial position
basket_width, basket_height = 100, 50
basket_x = (width - basket_width) // 2
basket_y = height - basket_height -20
basket_speed = 10

# Fruit dimensions and initial position
fruit_width, fruit_height = 30, 30
fruit_speed = 5
fruit_image = pygame.image.load("apple.jpg")
fruit_image = pygame.transform.scale(fruit_image, [fruit_width,fruit_height])

# Clock to control frame rate
clock = pygame.time.Clock()
def display_score(score):
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

# Main game loop
score = 0

# Initial position for the fruit
fruit_x = random.randint(0, width - fruit_width)
fruit_y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # move the basket
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and basket_x > 0:
                basket_x -= basket_speed
            if event.key == pygame.K_RIGHT  and basket_x < width - basket_width:
                basket_x += basket_speed

    fruit_y += fruit_speed

    if (basket_x < fruit_x < basket_x + basket_width and basket_y < fruit_y < basket_y + basket_width):
        fruit_x = random.randint(0,width - fruit_width)
        fruit_y = 0
        score += 1

    elif fruit_y > height:
        fruit_x = random.randint(0, width - fruit_width)
        fruit_y = 0
        score -= 1

    screen.fill(black)

    pygame.draw.rect(screen,white,(basket_x,basket_y,basket_width,basket_height,))
    display_score(score)
    screen.blit(fruit_image,(fruit_x,fruit_y))
    pygame.display.flip()
    clock.tick(30)