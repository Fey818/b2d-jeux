import pymongo
import entity
from player import Player
import vague
from item import Item, Equipable, Consumable
import db_init

class Game:
    def __init__(self, player: Player, vague: vague.Vague, mongo_client):
        self.player = player
        self.vague = vague
        self.mongo_client = mongo_client
    #SAUVEGARDER LA PARTIE DU JEU DANS LA BASE DE DONNÉES
    def savegame(self, save_name: str):
        db = db_init.connect_db()
        saves_collection = db["saves"]
        save_data = {
            "save_name": save_name,
            "player": self.player.__dict__,
            "vague": self.vague.__dict__
        }
        saves_collection.insert_one(save_data)

    def loadgame(self, save_name: str):
        db = db_init.connect_db()
        saves_collection = db["saves"]

        save_data = saves_collection.find_one({"save_name": save_name})
        if save_data:
            self.player = Player(**save_data["player"])
            self.vague = vague.Vague(**save_data["vague"])
        else:
            print(f"No save found with name: {save_name}")
#lancer le jeu
# demander le nom
# demander de cree equipe
#lancer la vague
    def launchgame(self):
        save_name = input("Enter save name: ")
        self.loadgame(save_name)
        

        
    def showleaderboard(self, top_n: int = 10):
        db = db_init.connect_db()
        saves_collection = db["saves"]
        leaderboard = saves_collection.find().sort("player.score", -1).limit(top_n)
        print("Leaderboard:")
        for idx, save in enumerate(leaderboard, start=1):
            player_name = save["player"]["name"]
            player_score = save["player"]["score"]
            print(f"{idx}. {player_name} - Score: {player_score}")

    def exitgame(self):
        print("Exiting game.")
        exit()


#lancer le menu principal du jeu avec 3 choix
    def main_menu(self):
        while True:
            print("Main Menu:")
            print("1. Start Game")
            print("2. Show Leaderboard")
            print("3. Exit Game")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.launchgame()
            elif choice == "2":
                self.showleaderboard()
            elif choice == "3":
                self.exitgame()
            else:
                print("Invalid choice. Please try again.")



