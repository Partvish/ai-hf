import pygame
import random

class Enemy:
    def __init__(self, width, height):
        self.size = 30
        self.x = random.randint(0, width - self.size)
        self.y = height - self.size
        self.speed = 3
        self.width = width
        self.height = height

    def update(self):
        self.y += self.speed
        if self.y > self.height:
            self.y = 0
            self.x = random.randint(0, self.width - self.size)

    def draw(self, screen):
        pygame.draw.polygon(
            screen, (139, 69, 19),
            [(self.x, self.y), (self.x + self.size, self.y), (self.x + self.size // 2, self.y + self.size)]
        )
