import entity
import item

class Player(entity.Entity):
    def __init__(self, name, score : int, team , inventory ):
        super().__init__(name, team[0].hp, team[0].maxHp, team[0].attack, team[0].defense)
        self.score = score
        self.team = team
        self.inventory = inventory
    def IsTeamAlive(self):
        return any(member.IsAlive() for member in self.team)

    def CheckInventory(self, item: item.Item = None):
        if item:
            if item in self.inventory:
                print(f"{item.name}: {item.description}")
            else:
                print(f"{item.name} is not in the inventory.")
        else:
            if not self.inventory:
                print("Inventory is empty.")
            else:
                for item in self.inventory:
                    print(f"{item.name}: {item.description}")

    
    def UseItem(self, item: item.Item):
        if item not in self.inventory:
            print(f"{item.name} is not in the inventory.")
            return
        if isinstance(item, item.Equipable):
            for member in self.team:
                member.EquipItem(item)
        elif isinstance(item, item.Consumable):
            for member in self.team:
                item.Use(member)
        self.inventory.remove(item)

    