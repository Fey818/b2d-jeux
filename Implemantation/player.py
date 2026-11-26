from db_init import CharacterList
from entity import Entity , Character
from item import Item, Equipable, Consumable

class Player(Entity):
    def __init__(self, name , score , team: list[Character], inventory: list[Item]):
        super().__init__(name, team[0].hp, team[0].maxHp, team[0].attack, team[0].defense)
        self.score = score
        self.team = team
        self.inventory = inventory

    def CreateTeam(self, team_size: int = 3):
        self.team = []
        for i, character in enumerate(CharacterList):
            if i >= team_size:
                break
            self.team.append(character)

    def PickCharacter(self):
        for character in CharacterList:
            self.team.append(character)
        self.team = list(set(self.team))

    
    def IsTeamAlive(self):
        return any(member.IsAlive() for member in self.team)

    def CheckInventory(self, item: Item = None):
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

    def UseItem(self, item: Item):
        if item not in self.inventory:
            print(f"{item.name} is not in the inventory.")
            return
        if isinstance(item, Equipable):
            for member in self.team:
                member.EquipItem(item)
        elif isinstance(item, Consumable):
            for member in self.team:
                item.Use(member)
        self.inventory.remove(item)