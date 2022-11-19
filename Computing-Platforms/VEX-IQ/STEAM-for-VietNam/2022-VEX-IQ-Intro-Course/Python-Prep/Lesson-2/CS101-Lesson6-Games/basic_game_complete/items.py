class RAM:
    def __init__(self, x, y, word):
        self.sprite_path = "sprites/ram.png"
        self.x = x
        self.y = y
        self.hp_change = 10

        self.word = word

    def get_info(self):
        return "New word: " + self.word


class Spark:
    def __init__(self, x, y):
        self.sprite_path = "sprites/spark.png"
        self.x = x
        self.y = y
        self.hp_change = -30

    def get_info(self):
        return "Spark!"
