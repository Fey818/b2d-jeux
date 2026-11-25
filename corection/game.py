

class Entity:

    def __init__(self, name, hp, maxHp, attack, defense):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.attack = attack
        self.defense = defense
    #boolean to check if the entity is alive
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

    def Attack(self, target : Entity):
        damage = self.attack - target.defense
        if damage < 0:
            damage = 0
        target.TakeDamage(damage)
        return damage
    def PlayTurn():
        pass