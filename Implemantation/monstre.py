import item

class Enemy:
    def __init__(self, dropable : list[item.Dropable]):
        self.dropable = dropable

    def drop_loot(self, item: list[item.Dropable]):
        dropped_items = []
        for i in item:
            if i in self.dropable:
                dropped_items.append(i)
        return dropped_items
    def PlayTurn(self, target):
        pass
    