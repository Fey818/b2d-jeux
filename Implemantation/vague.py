import player
import entity
import monstre
import character 
import random
import db_init


class Vague:
    def __init__(self, vague_actuelle: int , monsters : list):
        self.vague_actuelle = vague_actuelle
        self.monsters = monsters


    def pick_enemies(self, vague_actuelle: int):
        # Exemple de logique pour choisir les ennemis en fonction de la vague actuelle
        self.monsters = []
        for _ in range(vague_actuelle):
            monster = monstre.Monstre()  # Crée un monstre aléatoire
            self.monsters.append(monster)


    def tour_combat(self, monster: monstre.Monstre, player: player.Player):
        #tour de combat entre le monstre et l'équipe du joueur
        while monster.is_alive() and player.isteamalive():
            # faire attaquer le monstre puis l'équipe du joueur
            monster.attack(player.takedamageall())
            player.attack(monster)
    def play_vague(self, player: player.Player):
        score = 0
    
        for monster in self.monsters:
            #tant que le monstre est en vie et que l'équipe du joueur est encore en vie 
            
            while monster.is_alive() and player.isteamalive():
                #lancer un tour de combat entre le monstre et l'équipe du joueur
                self.tour_combat(monster, player)
            if not player.isteamalive():
                break
            if not monster.is_alive():
                score += 1
        return player.isteamalive(), score
                