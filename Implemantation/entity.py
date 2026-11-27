from db_init import database
class Entity:
    def __init__(self, name, hp, maxhp, attack, defense):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.attack = attack
        self.defense = defense

    def isalive(self):
        return self.hp > 0

    def takedamage(self, amount : int):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, amount : int):
        self.hp += amount
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return self.hp

    def attack(self, target : "Entity"):
        damage = self.attack - target.defense
        if damage < 0:
            damage = 0
        target.takedamage(damage)

    def playturn(self, target: "Entity"):
        self.attack(target)

    def __str__(self):
        return f"{self.name}: HP {self.hp}/{self.maxhp}, Attack {self.attack}, Defense {self.defense}"