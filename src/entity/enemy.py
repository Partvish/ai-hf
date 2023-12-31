import pygame
import random
from exceptions import DeathException, LeftTheScreenException
from entity.entity import Entity

class Enemy(Entity):
    def __init__(self, width, height, x=None, y=None):
        self.size = 30
        self.x = x or random.randint(0, width - self.size)
        self.y = y or self.size
        self.speed = random.randint(3, 6) 
        self.width = width
        self.height = height

        self.image = pygame.image.load("assets/goomba.bmp")
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def update(self):
        self.y += self.speed
        if self.y > self.height:
            raise LeftTheScreenException("")

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def handle_collision(self, other, em):
        raise DeathException("")
