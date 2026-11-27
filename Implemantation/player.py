import entity
import item
import monstre
import pymongo
import db_init
class Player(entity.Entity):
    def __init__(self, name, score : int, team , inventory ):
        super().__init__(name, team[0].hp, team[0].maxhp, team[0].attack, team[0].defense)
        self.score = score
        self.selected_characters = team
        self.inventory = inventory
    # Vérifie si l'un des membres de l'équipe est encore en vie
    def isteamalive(self):
        if any(member.isalive() for member in self.selected_characters):
            return True
        return False
    def pickcharacter(self):
        #montrer depuis la db game_db / Characters les personnages disponibles pour que le joueur choisisse pas plus de 3 personnages
        available_characters = list(db_init.connect_db().Characters.find())
        for i, character in enumerate(available_characters):
            print(f"{i + 1}. {character['name']}")
        selected_characters = []
        while len(selected_characters) < 3:
            choice = int(input("Choose a character by number: ")) - 1
            if 0 <= choice < len(available_characters):
                selected_characters.append(available_characters[choice])
            else:
                print("Invalid choice. Try again.")
        return selected_characters
    
    def isteamalive(self):
        return any(member.isalive() for member in self.selected_characters)

    def checkinventory(self, item: item.Item = None):
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

    #definir UseItem pour utiliser un objet de l'inventaire sur les personnages sélectionnés
    def useitem(self, item: item.Item):
        if item not in self.inventory:
            print(f"{item.name} is not in the inventory.")
            return
        if isinstance(item, item.Equipable):
            for member in self.selected_characters:
                member.EquipItem(item)
        elif isinstance(item, item.Consumable):
            for member in self.selected_characters:
                item.Use(member)
        self.inventory.remove(item)
 
#initialiser l'inventaire du joueur avec les objets disponibles depuis les item drop du monstre
    
    def initializeinventory(self, drop_loot: list[monstre.Enemy]):
        self.inventory = []
        for enemy in drop_loot:
            self.inventory.extend(enemy.drop_loot())

    
    