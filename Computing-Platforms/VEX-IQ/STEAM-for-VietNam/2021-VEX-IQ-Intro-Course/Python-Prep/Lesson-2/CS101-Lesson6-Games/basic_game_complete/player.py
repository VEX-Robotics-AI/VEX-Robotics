class Player:
    def __init__(self):
        self.sprite_path = "sprites/trau.png"

        self.x = 60
        self.y = 60

        self.speed = 5
        self.hp = 20
        self.items = []
        
    def pick_up_item(self, item):
        self.items.append(item)
        self.hp = self.hp + item.hp_change

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed

    def touch(self, obj2):
        offset_x = int(obj2.x - self.x)
        offset_y = int(obj2.y - self.y)
        return self.mask.overlap(obj2.mask, (offset_x, offset_y)) != None
