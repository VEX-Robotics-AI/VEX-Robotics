import random


# Cac hang so su dung trong file nay #
PLAYER_WIDTH = 25
PLAYER_HEIGHT = 44

TILE_WIDTH = 55
TILE_HEIGHT = 55


# Lop mo ta doi tuong Me Cung
class Maze:
    def __init__(self, maze_map, items_dict):
        self.bricks = []        # cac vien gach
        self.items = []         # cac do vat trong me cung (gom ca cac thanh RAM)
        self.ram_pieces = []    # cac thanh RAM trong me cung

        self.build_from_map(maze_map, items_dict)

    # Phuong thuc xay dung me cung tu mot ban do va mot tu dien do vat #
    def build_from_map(self, maze_map, items_dict):

        # Doc tung dong ban do
        row_index = 0
        while row_index < len(maze_map):
            # Doc tung ki tu trong dong do
            col_index = 0
            while col_index < len(maze_map[row_index]):
                if maze_map[row_index][col_index] == "W":
                    # Neu ki tu la "W" thi khoi tao mot vien gach Brick
                    brick = Brick(col_index * TILE_WIDTH, row_index * TILE_HEIGHT)
                    self.bricks.append(brick)
                else:
                    for item_type in ["$", "*", "0"]:
                        # Cho cac ki tu $, * hoac 0
                        if maze_map[row_index][col_index] == item_type:
                            # Neu ki tu trong ban do la 1 trong 3 ki tu tren
                            # thi lay 1 do vat tuong ung trong tu dien
                            # va cho do vat do vao danh sat do vat
                            item = items_dict[item_type].pop()
                            item.set_position(
                                col_index * TILE_WIDTH, row_index * TILE_HEIGHT
                            )
                            self.items.append(item)

                            if item_type == "$":
                                # Neu do vat do la 1 thanh RAM
                                # thi cung cho thanh RAM do vao mang ram_pieces
                                self.ram_pieces.append(item)

                col_index += 1
            row_index += 1

    # Phuong thuc bo mot do vat ra khoi me cung
    # dung khi nguoi choi nhat mot do vat
    def remove_item(self, item):
        self.items.remove(item)

        if item in self.ram_pieces:
            self.ram_pieces.remove(item)

    # Kiem tra xem nguoi choi da thang chua
    # Nguoi choi thang khi khong con thanh RAM nao trong me cung
    def check_winning(self):
        return len(self.ram_pieces) == 0

    # Kiem tra xem nguoi choi co dang di vao tuong (bricks) hay khong
    def check_hitting_wall(self, player):
        for brick in self.bricks:
            if brick.collide(player):
                return True

        return False


class Brick:

    def __init__(self, x, y):
        self.sprite_path = "sprites/fan.png"

        self.x = x
        self.y = y

    def collide(brick, player):
        # collide on top and left
        if (
            player.x >= brick.x
            and player.x <= brick.x + TILE_WIDTH
            and player.y >= brick.y
            and player.y <= brick.y + TILE_HEIGHT
        ):
            return True
        # collide on bottom and right
        if (
            player.x + PLAYER_WIDTH >= brick.x
            and player.x + PLAYER_WIDTH <= brick.x + TILE_WIDTH
            and player.y + PLAYER_HEIGHT >= brick.y
            and player.y + PLAYER_HEIGHT <= brick.y + TILE_HEIGHT
        ):
            return True
        # collide on top and right
        if (
            player.x + PLAYER_WIDTH >= brick.x
            and player.x + PLAYER_WIDTH <= brick.x + TILE_WIDTH
            and player.y >= brick.y
            and player.y <= brick.y + TILE_HEIGHT
        ):
            return True
        # collide on bottom and left
        if (
            player.x >= brick.x
            and player.x <= brick.x + TILE_WIDTH
            and player.y + PLAYER_HEIGHT >= brick.y
            and player.y + PLAYER_HEIGHT <= brick.y + TILE_HEIGHT
        ):
            return True

        return False
