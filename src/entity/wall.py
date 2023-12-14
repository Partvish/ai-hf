import pygame
from entity import Entity

class Wall(Entity):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self):
        self.y += self.speed
        if self.y > self.height:
            self.y = 0
            

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (self.x + self.size // 2, self.y + self.size // 2), self.size // 2)

    def handle_collision(self, other: Entity, em):
        em.add_score(50)
