import pygame
from entity.entity import Entity

class Player(Entity):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.size = 50
        self.speed = 5
        self.jump_height = 15
        self.gravity = 1
        self.is_jumping = False

        self.jump_image = pygame.image.load("assets/mario_jump.bmp")
        self.stand_image_r = pygame.image.load("assets/mario_stand.bmp")
        self.stand_image_l = pygame.image.load("assets/mario_stand.bmp")
        self.jump_image = pygame.transform.scale(self.jump_image, (self.size, self.size))
        self.stand_image_r = pygame.transform.scale(self.stand_image_r, (self.size, self.size))
        self.stand_image_l = pygame.transform.scale(self.stand_image_l, (self.size, self.size))
        self.stand_image_l = pygame.transform.flip(self.stand_image_l, True, False)
        self.stand_image = self.stand_image_r

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
            self.stand_image = self.stand_image_l
        if keys[pygame.K_RIGHT] and self.x < self.width - self.size:
            self.x += self.speed
            self.stand_image = self.stand_image_r
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True

    def update(self):
        if self.is_jumping:
            self.y -= self.jump_height
            self.jump_height -= self.gravity
            if self.jump_height < -15:
                self.is_jumping = False
                self.jump_height = 15

    def draw(self, screen):
        if self.is_jumping:
            screen.blit(self.jump_image, (self.x, self.y))
        else:
            screen.blit(self.stand_image, (self.x, self.y))

    def check_collision(self, entity):
        return (
            self.x < entity.x + entity.size
            and self.x + self.size > entity.x
            and self.y < entity.y + entity.size
            and self.y + self.size > entity.y
        )
