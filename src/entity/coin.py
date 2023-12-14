import pygame
import random
from entity.entity import Entity
from exceptions import LeftTheScreenException

class Coin(Entity):
    def __init__(self, width, height, x = None, y = None):
        self.size = 20
        self.x = x or random.randint(0, width - self.size)
        self.y = y or  self.size
        self.speed = random.randint(3, 6)  # No vertical movement for coins
        self.width = width
        self.height = height

    def update(self):
        self.y += self.speed
        if self.y > self.height:
            raise LeftTheScreenException("")

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (self.x + self.size // 2, self.y + self.size // 2), self.size // 2)

    def handle_collision(self, other: Entity, em):
        em.add_score(50)
