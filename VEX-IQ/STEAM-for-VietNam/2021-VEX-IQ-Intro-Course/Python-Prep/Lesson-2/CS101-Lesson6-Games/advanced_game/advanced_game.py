from pygame.locals import K_RIGHT, K_LEFT, K_UP, K_DOWN

from items import RAM, Spark
from game import Game
from maze import Maze
from player import Player


class AdvancedGame(Game):
    def __init__(self, maze_map, items_dict):
        # Khoi tao doi tuong nguoi choi
        self.player = Player()

        # Khoi tao doi tuong me cung
        self.maze = Maze(maze_map, items_dict)

        # Ket qua cua game: "lost" hoac "won"
        self.game_result = None

    # Phuong thuc chinh de chay game
    def run(self):
        self.start_game()  # bat dau tro choi

        while True:  # vong lap vo tan
            if self.check_if_user_quit():  # neu nguoi choi chon thoat ra khoi game
                self.close_window()        # dong cua so game
                break                      # thoat khoi vong lap vo tan

            if self.playing:  # neu game chua ket thuc
                key = self.get_key_pressed()  # lay ki tu ban phim nguoi choi vua nhan vao

                if key[K_RIGHT]:  # neu nguoi choi nhan phim sang phai
                    self.player.moveRight()  # di chuyen nguoi choi sang phai
                    if self.maze.check_hitting_wall(self.player):  # neu nguoi choi cham vao tuong
                        self.player.moveLeft()  # di chuyen nguoi choi vao vi tri cu

                if key[K_LEFT]:  # neu nguoi choi nhan phim sang trai
                    self.player.moveLeft()  # di chuyen nguoi choi sang trai
                    if self.maze.check_hitting_wall(self.player):  # neu nguoi choi cham vao tuong
                        self.player.moveRight()  # di chuyen nguoi choi vao vi tri cu

                if key[K_UP]:  # neu nguoi choi nhan phim len
                    self.player.moveUp()  # di chuyen nguoi choi len tren
                    if self.maze.check_hitting_wall(self.player):  # neu nguoi choi cham vao tuong
                        self.player.moveDown()  # di chuyen nguoi choi ve vi tri cu

                if key[K_DOWN]:  # neu nguoi choi nhan phim xuong
                    self.player.moveDown()  # di chuyen nguoi choi xuong duoi
                    if self.maze.check_hitting_wall(self.player):  # neu nguoi choi cham vao tuong
                        self.player.moveUp()  # di chuyen nguoi choi ve vi tri cu

                for item in self.maze.items:  # kiem tra tung do vat trong me cung
                    if self.player.touch(item):  # neu nguoi choi cham vao do vat nay
                        self.player.pick_up_item(item)  # yeu cau nguoi choi nhat do vat do len
                        self.maze.remove_item(item)  # yeu cau me cung loai bo vat do ra khoi me cung

                self.check_game_over()  # kiem tra xem game dang ket thuc chua
                self.draw_new_frame()   # ve frame ke tiep


    # Phuong thuc kiem tra xem game da ket thuc chua
    def check_game_over(self):
        if self.player.hp <= 0:        # neu HP cua nguoi choi bang 0 hoac am
            self.game_result = "lost"  # nguoi choi thua
            self.stop_game()           # ket thuc game

        elif self.maze.check_winning():    # yeu cau maze kiem tra xem da het cac thanh RAM chua
            self.game_result = "won"            # nguoi choi thang
            self.stop_game()                    # ket thuc game

    # Phuong thuc ve frame ke tiep
    def draw_new_frame(self):
        self.draw_background()     # ve background
        self.draw_maze()           # ve me cung
        self.draw_player()         # ve nguoi choi
        self.draw_player_hp()      # ve HP cua nguoi choi
        self.draw_player_items()   # ve do vat nguoi choi nhat duoc
        self.draw_game_result()    # ve ket qua cua game

        self.show_new_frame()      # hien thi frame vua ve

# Ban do cua game
maze_map = [
    "WWWWWWWWWW",
    "W    * $ W",
    "W  *   $ W",
    "W WWWWWW W",
    "W*W  $* $W",
    "W$W WWWW W",
    "W    $   W",
    "WWWWWWWWWW",
]

# Tu dien cac do vat
items_dict = {
    "$": [
        RAM("self"),
        RAM("method"),
        RAM("object"),
        RAM("class"),
        RAM("attribute"),
        RAM("self"),
    ],
    "*": [Spark(), Spark(), Spark(), Spark()]
}

# Khoi tao game
maze_game = AdvancedGame(maze_map, items_dict)

# Chay game
maze_game.run()
