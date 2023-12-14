from entity.enemy import Enemy
from entity.coin import Coin
from entity.entity import Entity
from exceptions import LeftTheScreenException

class EntityManager:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.score = 0
        self.entities = []
        self.generate_entities()

    def update(self):
        for entity in self.entities:
            try:
                entity.update()
            except LeftTheScreenException:
                self.entities.remove(entity)


    def draw(self, screen):
        for entity in self.entities:
            entity.draw(screen)

    def check_collisions(self, player):
        for entity in self.entities:
            if player.check_collision(entity):
                entity.handle_collision(player, self)
                self.entities.remove(entity)

    def generate_entities(self):
        for i in range(8):
            self.entities.append(Enemy(self.width, self.height))
        for i in range(5):
            self.entities.append(Coin(self.width, self.height))

    def add_score(self, score):
        self.score += score