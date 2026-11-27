import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")


class Entity:
    def __init__(self, name, hp, maxHp, attack, defense):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.attack = attack
        self.defense = defense

    def IsAlive(self):
        return self.hp > 0

    def TakeDamage(self, amount : int):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def Heal(self, amount : int):
        self.hp += amount
        if self.hp > self.maxHp:
            self.hp = self.maxHp
        return self.hp

    def Attack(self, target : "Entity"):
        damage = self.attack - target.defense
        if damage < 0:
            damage = 0
        target.TakeDamage(damage)

    def PlayTurn(self, target: "Entity"):
        self.Attack(target)

    def __str__(self):
        return f"{self.name}: HP {self.hp}/{self.maxHp}, Attack {self.attack}, Defense {self.defense}"