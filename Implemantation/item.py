import entity
import pymongo
import db_init
class Item:
    #class pour tout ralier a la base de données des items et initialiser les objets depuis la base de données
    def __init__(self, name, description, rarity, item_type, stats):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.item_type = item_type
        self.stats = stats 
    #class pour les objets de base si dans la db le type d'objet Equipable

class Equipable(Item):
    def __init__(self, name, description, rarity, item_type, stats, slot):
        super().__init__(name, description, rarity, item_type, stats)
        self.slot = slot


    #class pour les objets consumables si dans la db le type d'objet est Consumable true 
class Consumable(Item):
    def __init__(self, name, description, rarity, item_type, stats): 
        super().__init__(name, description, rarity, item_type, stats)

    def Use(self, target: entity.Entity):
        if "hp" in self.stats:
            target.heal(self.stats["hp"])
        if "attack" in self.stats:
            target.attack += self.stats["attack"]
        if "defense" in self.stats:
            target.defense += self.stats["defense"]