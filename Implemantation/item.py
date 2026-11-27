import entity
class Item:
    def __init__(self, name ,description : str , rarity : int ,item_type : str , Stats : dict):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.item_type = item_type
        self.stats = Stats

class Equipable(Item):
    def __init__(self, name, description, rarity, item_type, Stats, slot):
        super().__init__(name, description, rarity, item_type, Stats)
        self.slot = slot


class Consumable(Item):
    def __init__(self, name, description, rarity, item_type, Stats): 
        super().__init__(name, description, rarity, item_type, Stats)

    def Use(self, target: entity.Entity):
        if "hp" in self.stats:
            target.Heal(self.stats["hp"]) 