from entity import Entity , Character
from item import Item, Equipable, Consumable

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


class Vague:
    def __init__(self, vague_actuelle : int, enemies: list[Entity]):
        self.vague_actuelle = vague_actuelle
        self.enemies = enemies

    def PickEnnemies(self, vague : Vague):
        # Example logic to pick enemies based on the current wave
        self.enemies = [enemy for enemy in self.enemies if enemy.IsAlive()]

    def Playvague(self, player: Player):
        for enemy in self.enemies:
            while enemy.IsAlive() and player.IsAlive():
                player.Attack(enemy)
                if enemy.IsAlive():
                    enemy.Attack(player)
        return player.IsAlive()

    def GetDifficulty(self):
        # Example logic to determine difficulty based on the current wave
        return self.vague_actuelle * 10
    

    
