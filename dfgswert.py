class Goblin:
    def __init__(self, name, damage, hp) -> None:
        self.name = name
        self.damage = damage
        self.hp = hp

    def attack(self, target):
        print(f'Goblin {self.name} attacks {target.name}')
        target.hp -= self.damage

    def __str__(self) -> str:
        return f'Name: {self.name}\n\tDamage: {self.damage}\n\tHealth: {self.hp}'
    

class Vampire:
    def __init__(self, name, damage, hp) -> None:
        self.name = name
        self.damage = damage
        self.hp = hp

    def attack(self, target):
        print(f'Vampire {self.name} attacks {target.name}')
        target.hp -= self.damage

    def life_steal(self, target):
        print(f'Vampire {self.name} steals life from {target.name}')
        target.hp -= 1
        self.hp += 5

    def __str__(self) -> str:
        return f'Name: {self.name}\n\tDamage: {self.damage}\n\tHealth: {self.hp}'