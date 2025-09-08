import random
from enemy import Enemy

def ice_arrow(self):
    raise NotImplementedError

class BossElf (Enemy):
    def __init__(self, name, color):
        super().__init__(name)
        self.health = 200
        self.attack_power = 55
        self.color = "white"

    def roar(self):
        print(f"{self.name}" "screamed that you WILL die!") 
    
    def ice_arrow(self):
        print(f"{self.name} shoots an ice arrow at you!")
        return self.attack_power + 20

    def attack(self):
           choice = random.choice("ice Arrows", "snowballs")
           if choice == "ice Arrows":
               ice_arrow()
           else:
                print(f"{self.name} throws a snowball at you!")
           return self.attack_power(self.attack_power)
    
    def enrage(self):
         if self.health <= 25:
                print(f"{self.name} is enraged (attacks with double power!)")
                self.attack_power = 110
                return(self.attack_power)
