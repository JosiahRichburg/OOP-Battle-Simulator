from enemy import Enemy

class Goblin(Enemy):  
    def _init_(self, name, color):
        super()._init_(name)
        (self.color) = color
        self.health = 80
