import pygame
import sys
from player import Player
from entities import EntitiesManager

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Mario Game")
clock = pygame.time.Clock()

# Player
player = Player(WIDTH // 2 - 25, HEIGHT - 70, WIDTH, HEIGHT)

# Entities
entities_manager = EntitiesManager(WIDTH, HEIGHT, player.y)

# Score
score = 0
font = pygame.font.SysFont(None, 30)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.handle_input()

    # Update entities
    player.update()
    entities_manager.update()

    # Check collisions
    collision, collision_type = entities_manager.check_collisions(player)
    if collision:
        if collision_type == "enemy":
            game_over_text = font.render("Game Over", True, WHITE)
            screen.blit(game_over_text, (WIDTH // 2 - 50, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.delay(2000)  # Pause for 2 seconds
            running = False
        elif collision_type == "coin":
            score += 50
            entities_manager.reset_coins(player.y)

    # Draw background
    screen.fill(BLUE)

    # Draw entities
    player.draw(screen)
    entities_manager.draw(screen)

    # Draw score
    score_text = font.render("Score: {}".format(score), True, WHITE)
    screen.blit(score_text, (WIDTH - 150, 20))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
