from enemy import Enemy
from coin import Coin

class EntitiesManager:
    def __init__(self, width, height, player_y):
        self.width = width
        self.height = height
        self.enemies = [Enemy(width, height) for _ in range(3)]
        self.coins = [Coin(width, height, player_y) for _ in range(5)]

    def update(self):
        for enemy in self.enemies:
            enemy.update()
        for coin in self.coins:
            coin.update()

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        for coin in self.coins:
            coin.draw(screen)

    def check_collisions(self, player):
        for enemy in self.enemies:
            if player.check_collision(enemy):
                return True, "enemy"
        for coin in self.coins:
            if player.check_collision(coin):
                return True, "coin"
        return False, None

    def reset_coins(self, player_y):
        for coin in self.coins:
            coin.reset(player_y)
