import pygame
import sys
import random
from pygame.locals import K_ESCAPE, QUIT

# Dinh nghia cac hang so cho game #
WIDTH = 800
HEIGHT = 450
INFO_BOARD_X = 580

FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PLAYER_WIDTH = 25
PLAYER_HEIGHT = 44

ITEM_WIDTH = 40
ITEM_HEIGHT = 40

TILE_WIDTH = 55
TILE_HEIGHT = 55


# Lop chinh de chay game #
class Game:

    # Phuong thuc khoi tao chuong trinh pygame #
    def start_game(self):
        pygame.init()

        # clock dung de dieu khien FPS
        self.clock = pygame.time.Clock()

        # Khoi tao cua so game
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE)

        # Khoi tao font chu de viet thong so len man hinh game
        self.font = pygame.font.SysFont("Times New Roman", 25)

        self.playing = True # True: Game dang chay. False: Dung game

        # Load hinh anh nhan vat nguoi choi
        self.prepare_player()

        for brick in self.maze.bricks:  # load hinh anh tuong trong me cung
            self.prepare_brick(brick)
        for item in self.maze.items:    # load hinh anh cac do vat trong me cung
            self.prepare_item(item)

    # Phuong thuc kiem tra xem nguoi choi co nhan vao nut thoat game hay khong #
    def check_if_user_quit(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return True

        keys = self.get_key_pressed()
        if keys[K_ESCAPE]:
            return True

        return False

    # Dung game #
    def stop_game(self):
        self.playing = False

    # Dong cua so game #
    def close_window(self):
        pygame.quit()

    # Phuong thuc khoi tao chuong trinh pygame #
    def get_key_pressed(self):
        return pygame.key.get_pressed()

    # Hien thi tat ca cac doi tuong ra man hinh game #
    def show_new_frame(self):
        pygame.display.flip()
        self.clock.tick(FPS)

    # Hien thi background ra man hinh game #
    def draw_background(self):
        self.screen.fill(BLACK)
        self.background = pygame.image.load("sprites/background.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (560, 440))
        self.screen.blit(self.background, (0, 0))

    # Ve nhan vat nguoi choi vao man hinh game #
    def draw_player(self):
        self.screen.blit(self.player.sprite, (self.player.x, self.player.y))

    # Ve me cung ra man hinh game #
    def draw_maze(self):
        for brick in self.maze.bricks: # ve tuong
            self.screen.blit(brick.sprite, (brick.x, brick.y))
        for item in self.maze.items: # ve item
            self.screen.blit(item.sprite, (item.x, item.y))

    # Viet cac do vat nguoi choi nhat duoc ra man hinh game #
    def draw_player_items(self):
        info_board_y = 60
        for item in self.player.items:
            info = self.font.render(item.get_info(), 1, WHITE)
            self.screen.blit(info, (INFO_BOARD_X, info_board_y))
            info_board_y += 30

    # Viet ket qua ra man hinh game #
    def draw_game_result(self):
        result_y = 60 + len(self.player.items) * 30
        if self.game_result == "won":
            win = self.font.render("YOU WON!!", 1, WHITE)
            self.screen.blit(win, (INFO_BOARD_X, result_y))
        elif self.game_result == "lost":
            lose = self.font.render("YOU LOST!!", 1, WHITE)
            self.screen.blit(lose, (INFO_BOARD_X, result_y))

    # Viet HP cua nhan vat ra man hinh game #
    def draw_player_hp(self):
        hp = self.font.render("HP: " + str(self.player.hp), 1, WHITE)
        self.screen.blit(hp, (INFO_BOARD_X, 20))

    # Tai hinh anh nhan vat nguoi choi len doi tuong Player #
    def prepare_player(self):
        sprite = pygame.image.load(self.player.sprite_path).convert_alpha()
        self.player.sprite = pygame.transform.scale(
            sprite, (PLAYER_WIDTH, PLAYER_HEIGHT)
        )
        self.player.mask = pygame.mask.from_surface(self.player.sprite)

    # Tai hinh anh tuong len doi tuong Tile #
    def prepare_brick(self, brick):
        sprite = pygame.image.load(brick.sprite_path).convert_alpha()
        brick.sprite = pygame.transform.scale(sprite, (TILE_WIDTH, TILE_HEIGHT))
        brick.mask = pygame.mask.from_surface(brick.sprite)

    # Tai hinh anh item len doi tuong Item #
    def prepare_item(self, item):
        sprite = pygame.image.load(item.sprite_path).convert_alpha()
        item.sprite = pygame.transform.scale(sprite, (ITEM_WIDTH, ITEM_HEIGHT))
        item.mask = pygame.mask.from_surface(item.sprite)
