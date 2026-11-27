import pymongo
import entity
from player import Player, Vague
from item import Item, Equipable, Consumable
client = pymongo.MongoClient("mongodb://localhost:27017/")
def connect_db():
    db = client["game_db"]
    return db




class Game:
    def __init__(self, player: Player, vague: Vague, mongo_client):
        self.player = player
        self.vague = vague
        self.mongo_client = mongo_client

    def SaveGame(self, save_name: str):
        db = self.mongo_client["game_db"]
        saves_collection = db["saves"]
        save_data = {
            "save_name": save_name,
            "player": self.player.__dict__(),
            "vague": self.vague.__dict__()
        }
        saves_collection.insert_one(save_data)

    def LoadGame(self, save_name: str):
        db = self.mongo_client["game_db"]
        saves_collection = db["saves"]

        save_data = saves_collection.find_one({"save_name": save_name})
        if save_data:
            self.player = Player(**save_data["player"])
            self.vague = Vague(**save_data["vague"])
        else:
            print(f"No save found with name: {save_name}")

    def LaunchGame(self):
        print("Game launched.")
        print(f"Player: {self.player.name}")
        print(f"Vague: {self.vague.number}")
        print(f"Team: {[character.name for character in self.player.team]}")
        print(f"Inventory: {[item.name for item in self.player.inventory]}")
        print(f"Score: {self.player.score}")

    def ShowLeaderboard(self, top_n: int = 10):
        db = self.mongo_client["game_db"]
        saves_collection = db["saves"]
        leaderboard = saves_collection.find().sort("player.score", -1).limit(top_n)
        print("Leaderboard:")
        for idx, save in enumerate(leaderboard, start=1):
            player_name = save["player"]["name"]
            player_score = save["player"]["score"]
            print(f"{idx}. {player_name} - Score: {player_score}")

    def ExitGame(self):
        print("Exiting game.")
        exit()