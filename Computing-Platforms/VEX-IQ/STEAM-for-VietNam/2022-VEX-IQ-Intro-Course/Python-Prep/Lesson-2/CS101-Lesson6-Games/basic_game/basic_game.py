from pygame.locals import K_RIGHT, K_LEFT, K_UP, K_DOWN

from game import Game
from player import Player
from items import RAM, Spark


class BasicGame(Game):
    def __init__(self):
        # Khoi tao doi tuong nguoi choi
        self.player = Player()

        # Khoi tao doi tuong do vat
        self.items = [
            RAM(125, 100, "object"),
            RAM(150, 250, "attribute"),
            RAM(200, 150, "method"),
            Spark(75, 100),
            Spark(300, 100),
        ]

        # Ket qua cua game
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
                    self.player.moveRight()

                if key[K_LEFT]:  # neu nguoi choi nhan phim sang phai
                    self.player.moveLeft()

                if key[K_UP]:  # neu nguoi choi nhan phim sang phai
                    self.player.moveUp()

                if key[K_DOWN]:  # neu nguoi choi nhan phim xuong
                    self.player.moveDown()

                for item in self.items:  # kiem tra tung do vat
                    if self.player.touch(item):  # neu nguoi choi cham vao do vat nay
                        print("lam sao de nguoi choi nhat len 1 do vat?")

                self.check_game_over()  # kiem tra xem game dang ket thuc chua
                self.draw_new_frame()   # ve frame ke tiep

    # Phuong thuc kiem tra xem game da ket thuc chua
    def check_game_over(self):
        if self.player.hp <= 0:        # neu HP cua nguoi choi bang 0 hoac am
            self.game_result = "lost"  # nguoi choi thua
            self.stop_game()           # ket thuc game

        elif self.count_ram() == 0:    # neu khong con thanh RAM nao trong game
            self.game_result = "won"   # nguoi choi thang
            self.stop_game()           # ket thuc game

    # Phuong thuc dem cac thanh RAM con lai trong game
    def count_ram(self):
        count = 0
        for item in self.items:
            if isinstance(item, RAM):  # item co phai la doi tuong cua lop RAM khong?
                count = count + 1
        return count

    # Phuong thuc ve frame ke tiep
    def draw_new_frame(self):
        self.draw_background()     # ve background
        self.draw_items()          # ve do vat
        self.draw_player()         # ve nguoi choi
        self.draw_player_hp()      # ve HP cua nguoi choi
        self.draw_player_items()   # ve do vat nguoi choi nhat duoc
        self.draw_game_result()    # ve ket qua cua game

        self.show_new_frame()      # hien thi frame vua ve


game = BasicGame()
game.run()
