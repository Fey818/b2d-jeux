from db_init import *
from entity import *
from player import Player, Vague
from item import Item, Equipable, Consumable

class Game:
    def __init__(self, player: Player, vague: Vague, mongo_client):
        self.player = player
        self.vague = vague
        self.mongo_client = mongo_client
    #tout ce qui est nécessaire pour sauvegarder le jeu
    def SaveGame(self):
        self.mongo_client.save_game(self.player, self.vague)
        
