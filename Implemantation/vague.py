from entity import *
class Vague:
    def __init__(self, vague_actuelle: int , monsters : list):
        self.vague_actuelle = vague_actuelle
        self.monsters = monsters

    def PickEnemies(self, vague : Vague):
        return vague.monsters

    def GetDifficulty(self, vague : Vague):
        return int(vague.vague_actuelle)
