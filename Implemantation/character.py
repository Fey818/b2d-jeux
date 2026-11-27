import entity
import item
import player
import pymongo
import db_init
class Character(entity.Entity):
    #equipable items for the character depuis l'inventaire du jeu dans player
    def __init__(self, attack: int , defense: int , equipable: list[item.Equipable]):
        self.attack = attack
        self.defense = defense
        self.equipable = equipable
        self.current_health = 100 
    #definir EquipItem pour équiper un objet dans l'inventaire du personnage
    def EquipItem(self, item: item.Equipable):
        if item in self.equipable:
            self.attack += item.attack
            self.defense += item.defense
            print(f"Equipped {item.name}: +{item.attack} attack, +{item.defense} defense")
        else:
            print(f"{item.name} cannot be equipped.")

    def UnequipItem(self, item: item.Equipable):
        if item in self.equipable:
            self.attack -= item.attack
            self.defense -= item.defense
            print(f"Unequipped {item.name}: -{item.attack} attack, -{item.defense} defense")
        else:
            print(f"{item.name} is not equipped.")


    def IsSlotAvailable(self, slot_name: str):
        for item in self.equipable:
            if item.slot == slot_name:
                return False
        return True


    def GetEquippedItems(self, slot_name: str):
        equipped_items = []
        for item in self.equipable:
            if item.slot == slot_name:
                equipped_items.append(item)
        return equipped_items

    def ProjectDamage(self, target: entity.Entity) -> int:
        # Calculate projected damage against the target
        damage = max(0, self.attack - target.defense)
        return damage

    def TakeDamage(self, damage: int):
        self.current_health -= damage
        if self.current_health <= 0:
            self.current_health = 0
            print(f"{self} has been defeated.")

    def play_turn(self, target: entity.Entity):
        #choisir si attaque ou utilisation d'objet
        action = input("Choose action (attack/use item): ").strip().lower()
        if action == "attack":
            damage = self.ProjectDamage(target)
            print(f"{self} attacks {target} for {damage} damage.")
            target.TakeDamage(damage)
        elif action == "use item":
            print("Item usage not implemented yet.")
        else:
            print("Invalid action.")
