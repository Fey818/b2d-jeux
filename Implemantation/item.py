from db_init import *
from entity import Entity
class Item:
    def __init__(self, name ,description : str , drop_rate : int ,item_type : str , Stats : dict):
        self.name = name
        self.description = description
        self.drop_rate = drop_rate
        self.item_type = item_type
        self.stats = Stats

class Equipable(Item):
    def __init__(self, name, description, drop_rate, item_type, Stats, slot):
        super().__init__(name, description, drop_rate, item_type, Stats)
        self.slot = slot

class Consumable(Item):
    def __init__(self, name, description, drop_rate, item_type, Stats): 
        super().__init__(name, description, drop_rate, item_type, Stats)

    def Use(self, target: Entity):
        if "hp" in self.stats:
            target.Heal(self.stats["hp"])  