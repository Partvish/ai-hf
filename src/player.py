import pygame

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.size = 50
        self.speed = 5
        self.jump_height = 10
        self.gravity = 1
        self.is_jumping = False

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < self.width - self.size:
            self.x += self.speed
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True

    def update(self):
        if self.is_jumping:
            self.y -= self.jump_height
            self.jump_height -= self.gravity
            if self.jump_height < -10:
                self.is_jumping = False
                self.jump_height = 10

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.size, self.size))

    def check_collision(self, entity):
        return (
            self.x < entity.x + entity.size
            and self.x + self.size > entity.x
            and self.y < entity.y + entity.size
            and self.y + self.size > entity.y
        )
