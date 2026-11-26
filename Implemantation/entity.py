from item import Item, Equipable
from db_init import ItemList , ItemListDict

class Entity:

    def __init__(self, name, hp, maxHp, attack, defense):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.attack = attack
        self.defense = defense

    def IsAlive(self) :

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

    def PlayTurn(self, target: Entity):
        self.Attack(target)

class Character(Entity):
    def __init__(self, equipment : list[Equipable], attack : int , defense : int):
        super().__init__(equipment[0].name, equipment[0].stats["hp"], equipment[0].stats["maxHp"], attack, defense)
        self.equipped_items = equipment

    def EquipItem(self, item: Equipable):
        self.attack += item.stats["attack"]
        self.defense += item.stats["defense"]
        self.maxHp += item.stats["maxHp"]
        self.hp += item.stats["maxHp"]
        self.equipped_items.append(item)


    def UnequipItem(self, item: Equipable):
        if item in self.equipped_items:
            self.attack -= item.stats["attack"]
            self.defense -= item.stats["defense"]
            self.maxHp -= item.stats["maxHp"]
            if self.hp > self.maxHp:
                self.hp = self.maxHp
            self.equipped_items.remove(item)

    def IsSlotAvailable(self, slot_name: str):
        for item in self.equipped_items:
            if item.slot == slot_name:
                return False
        return True
    

    def GetEquipment(self , slot_name: str):
        equipable = None
        for item in self.equipped_items:
            if item.slot == slot_name:
                equipable = item
                break
        return equipable


    def ProjectDamage(self, target: Entity):
        damage = self.attack - target.defense
        if damage < 0:
            damage = 0
        return damage
    def PlayTurn(self, target: Entity): 
        self.Attack(target)


class Enemy(Entity):
    def __init__(self, name, hp, maxHp, attack, defense, dropable : list[Item]):
        super().__init__(name, hp, maxHp, attack, defense)
        self.dropable = dropable

    def PlayTurn(self, target: Entity ):
        self.Attack(target)
