import entity
import item
class Character(entity.Entity):
    def __init__(self, attack: int , defense: int , equipable: list[db]):
        self.attack = attack
        self.defense = defense
        self.equipable = equipable
        self.current_health = 100 

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
        damage = max(0, self.attack - target.defense)
        return damage

    def TakeDamage(self, damage: int):
        self.current_health -= damage
        if self.current_health <= 0:
            self.current_health = 0
            print(f"{self} has been defeated.")

    def play_turn(self, target: entity.Entity):
        damage = self.ProjectDamage(target)
        print(f"{self} attacks {target} for {damage} damage.")
        target.TakeDamage(damage)