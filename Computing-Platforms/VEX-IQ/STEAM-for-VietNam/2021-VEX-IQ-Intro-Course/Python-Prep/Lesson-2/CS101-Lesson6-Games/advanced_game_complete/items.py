class Item:
    def set_position(self, x, y):
        self.x = x
        self.y = y


class RAM(Item):
    def __init__(self, word):
        self.sprite_path = "sprites/ram.png"
        self.hp_change = 10

        self.word = word

    def get_info(self):
        return "New word: " + self.word


class Spark(Item):
    def __init__(self):
        self.sprite_path = "sprites/spark.png"
        self.hp_change = -30

    def get_info(self):
        return "Spark!"


class Robot(Item):
    def __init__(self, name):
        self.sprite_path = "sprites/tre.png"
        self.hp_change = 20

        self.name = name

    def get_info(self):
        return "Robot: " + self.name
