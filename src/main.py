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

background_image = pygame.image.load("assets/background.bmp")  # Replace "background.jpg" with your image file
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT+80 ))


# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Mario Game")
clock = pygame.time.Clock()

# Score
font = pygame.font.SysFont(None, 30)

# Set up a custom event for the timer
TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 500)
current_time = 0
spawn_time = 3000

menu_title = font.render("Simple AI Game", True, WHITE)
start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)
exit_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
button_color = (50, 50, 50)
button_hover_color = (100, 100, 100)


menu_screen = True



player = Player(WIDTH // 2 - 25, HEIGHT - 70, WIDTH, HEIGHT)
em = EntityManager(WIDTH, HEIGHT)

def init_game():
    global player
    global em
    global menu_screen
    global current_time
    global spawn_time
    player = Player(WIDTH // 2 - 25, HEIGHT - 70, WIDTH, HEIGHT)
    em = EntityManager(WIDTH, HEIGHT)
    current_time = 0
    spawn_time = 3000
    menu_screen = False

def render_game_screen():
    global player
    global em
    global menu_screen
    global current_time
    global spawn_time
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
        pygame.time.delay(1000)
        menu_screen = True

    screen.blit(background_image, (0, 0))

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

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == TIMER_EVENT:
            if not menu_screen:
                current_time += 500
                if current_time > spawn_time:
                    em.generate_entities()
                    current_time = 0
                    if spawn_time > 500:
                        spawn_time -= 100
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the mouse is clicked on the buttons
            if start_button.collidepoint(event.pos):
                init_game()
            elif exit_button.collidepoint(event.pos):
                running = False

    if menu_screen:
        # Draw menu screen
        screen.fill(BLUE)
        screen.blit(background_image, (0, 0))  # No need for panning on the menu screen
        screen.blit(menu_title, (WIDTH // 2 - menu_title.get_width() // 2, 100))

        # Draw start button
        pygame.draw.rect(screen, button_color, start_button)
        start_text = font.render("Start", True, WHITE)
        screen.blit(start_text, (start_button.x + start_button.width // 2 - start_text.get_width() // 2,
                                 start_button.y + start_button.height // 2 - start_text.get_height() // 2))

        # Draw exit button
        pygame.draw.rect(screen, button_color, exit_button)
        exit_text = font.render("Exit", True, WHITE)
        screen.blit(exit_text, (exit_button.x + exit_button.width // 2 - exit_text.get_width() // 2,
                                exit_button.y + exit_button.height // 2 - exit_text.get_height() // 2))
        pygame.display.flip()
    else:
        render_game_screen()
    

# Quit the game
pygame.quit()
sys.exit()
