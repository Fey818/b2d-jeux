import item
import random
import entity
import pymongo
import db_init

class Enemy:
    def __init__(self, dropable : list[item.Dropable]):
        self.dropable = dropable
    #definir drop loot chercher dans la db game_db / Items les objets que le monstre peut drop enregistrer dans l'inventaire du joueur
    def drop_loot(self):
        dropped_items = []
        available_items = list(db_init.connect_db().Items.find())
        for i in available_items:
            if i['name'] in [d.name for d in self.dropable]:
                dropped_items.append(i)
        return dropped_items

    #definir PlayTurn pour que le monstre joue son tour et attaque une cible aléatoire parmi les cible en vie
    def playturn(self, targets):
        #check dans is team alive pour ne cibler que les cibles en vie
        alive_targets = [t for t in targets if t.isalive()]
        if not alive_targets:
            return
        target = random.choice(alive_targets)
        # Implement the action against the chosen target
        target.takedamage(self.attack)