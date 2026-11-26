#ramener la base de donnée dans le jeu
from corection.test import Character
from db_init import *
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

    def Attack(self, target : Entity):
        damage = self.attack - target.defense
        if damage < 0:
            damage = 0
        target.TakeDamage(damage)

    def PlayTurn(self):
        pass

class Player(Entity):
    def __init__(self, name , score , Character : Character , inventory : list[Item]):
        super().__init__(name, Character.hp, Character.maxHp, Character.attack, Character.defense)
        self.score = score
        self.character = Character
        self.inventory = inventory

    def CreateTeam(self, name, hp, maxHp, attack, defense):
        return Character(name, hp, maxHp, attack, defense)

    def PickCharacter(self, character: Character):
        self.character = character
    
    def IsTeamAlive(self):
        return self.character.IsAlive()

    def CheckInventory(self):
        return self.inventory

    def UseItem(self, item: Item):
        if isinstance(item, Equipable):
            self.character.EquipItem(item)
        elif isinstance(item, Consumable):
            item.Use(self.character)

class Character(Entity):
    def __init__(self, Equipable : Equipable , attack : int , defense : int):
        super().__init__(Equipable.name, Equipable.hp, Equipable.maxHp, attack, defense)
        self.equipped_items = [Equipable]

    def EquipItem(self, item: Equipable):
        self.attack += item.attack
        self.defense += item.defense
        self.maxHp += item.maxHp
        self.hp += item.maxHp
        self.equipped_items.append(item)

    def UnequipItem(self, item: Equipable):
        if item in self.equipped_items:
            self.attack -= item.attack
            self.defense -= item.defense
            self.maxHp -= item.maxHp
            if self.hp > self.maxHp:
                self.hp = self.maxHp
            self.equipped_items.remove(item)

    def IsSlotAvailable(self, slot_name: str):
        for item in self.equipped_items:
            if item.slot == slot_name:
                return False
        return True

    def GetEquipment(self , slot_name: str):
        Equipable = None
        for item in self.equipped_items:
            if item.slot == slot_name:
                Equipable = item
                break
        return Equipable

    def ProjectDamage(self, target: Entity):
        damage = self.attack - target.defense
        if damage < 0:
            damage = 0
        return damage
    def PlayTurn(self):
        pass

class Item:
    def __init__(self, name ,description : str , drop_rate : int ,item_type : str , Stats : dict):
        