import pygame
import sys
from exceptions import DeathException
from entity.player import Player
from entity_manager import EntityManager

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
em = EntityManager(WIDTH, HEIGHT)

# Score
font = pygame.font.SysFont(None, 30)

# Set up a custom event for the timer
TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 500)
current_time = 0
spawn_time = 3000

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == TIMER_EVENT:
            current_time += 500
            if current_time > spawn_time:
                em.generate_entities()
                current_time = 0
                if spawn_time > 500:
                    spawn_time -= 100
    player.handle_input()

    # Update entities
    player.update()
    em.update()

    # Check collisions
    try:
        em.check_collisions(player)
    except DeathException:
        game_over_text = font.render("Game Over", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 50, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)  # Pause for 2 seconds
        running = False

    # Draw background
    screen.fill(BLUE)

    # Draw entities
    em.draw(screen)
    player.draw(screen)

    # Draw score
    score_text = font.render("Score: {}".format(em.score), True, WHITE)
    screen.blit(score_text, (WIDTH - 150, 20))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
