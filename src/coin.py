import pygame
import random

class Coin:
    def __init__(self, width, height, player_y):
        self.size = 20
        self.x = random.randint(0, width - self.size)
        self.y = player_y - self.size
        self.speed = 0  # No vertical movement for coins
        self.width = width
        self.height = height

    def update(self):
        pass  # Coins don't need to update in this case

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (self.x + self.size // 2, self.y + self.size // 2), self.size // 2)

    def reset(self, player_y):
        self.y = player_y - self.size
        self.x = random.randint(0, self.width - self.size)
