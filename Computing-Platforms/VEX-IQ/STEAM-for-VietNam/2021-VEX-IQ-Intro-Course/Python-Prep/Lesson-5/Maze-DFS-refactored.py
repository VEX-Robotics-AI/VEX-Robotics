"""
https://bit.ly/S4V_CS201_Maze_DFS
https://www.robotmesh.com/studio/60f105f1c4b0580fb15d4bc5

Cách sửa lỗi sau khi Copy Project:
Xoá tất cả nội dung trong các dòng từ
#region config (dòng 20)
đến
#endregion config
"""


# IMPORT CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ================================
import math

from vex import (
    Gyro, Motor, Ports, FORWARD, LEFT, RIGHT,
    Sonar   # Sonar = Cảm biến khoảng cách
)
from drivetrain import Drivetrain


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo các motor
motor_right = Motor(Ports.PORT1, True)   # reverse=True: đảo ngược chiều xoay
motor_left = Motor(Ports.PORT2)

# khởi tạo drivetrain với 2 motor, mỗi motor gắn một bánh xe
# chu vi 200mm và khoảng cách giữa 2 bánh xe 2 bên là 198mm
dt = Drivetrain(motor_left, motor_right, 200, 198)

# khởi tạo cảm biến khoảng cách
distance_sensor = Sonar(Ports.PORT7)

# khởi tạo cảm biến Gyro (phương hướng)
gyro = Gyro(Ports.PORT3)


# ĐỊNH NGHĨA HẰNG SỐ
# ===========================

# mm, khoảng cách robot cần di chuyển để tiến một ô trong mê cung
GRID_SIZE = 308

NORTH = 'N'
EAST = 'E'
WEST = 'W'
SOUTH = 'S'

# mã của các ô trong ma trận mê cung
DESTINATION_CODE = 3
OPEN_CODES = [1, 2, 3]   # khong phai tuong


# ĐỊNH NGHĨA CÁC HÀM
# ==================

# Hàm hỗ trợ di chuyển
def move_one_grid():
    dt.drive_for(FORWARD, GRID_SIZE)


# Hàm hỗ trợ di chuyển
def turn_to(new_direction):
    current_direction = fine_tune_and_get_direction()
    current_heading = get_target_heading(current_direction)
    new_heading = get_target_heading(new_direction)
    heading_diff = new_heading - current_heading
    if heading_diff > 0:
        dt.turn_for(LEFT, heading_diff)
    else:
        dt.turn_for(RIGHT, math.fabs(heading_diff))
    fine_tune_direction()


# Hàm hỗ trợ di chuyển
def get_target_heading(direction):
    if direction == NORTH:
        return 90
    if direction == EAST:
        return 0
    if direction == WEST:
        return 180
    if direction == SOUTH:
        return 270
    return None


def fine_tune_and_get_direction():
    fine_tune_direction()
    return get_direction()


def get_direction():
    heading = gyro.heading()
    if math.fabs(90 - heading) <= 30:
        return NORTH
    if math.fabs(180 - heading) <= 30:
        return WEST
    if math.fabs(270 - heading) <= 30:
        return SOUTH
    if math.fabs(0 - heading) <= 30 or math.fabs(360 - heading) <= 30:
        return EAST
    return None


# Hàm hỗ trợ di chuyển
def fine_tune_direction():
    direction = get_direction()
    heading = gyro.heading()
    if direction == NORTH:
        turn_dir = RIGHT if heading >= 90 else LEFT
        turn_deg = math.fabs(90-heading)
    elif direction == EAST:
        if heading < 90:
            turn_dir = RIGHT
            turn_deg = math.fabs(heading)
        else:
            turn_dir = LEFT
            turn_deg = math.fabs(360-heading)
    elif direction == WEST:
        turn_dir = RIGHT if heading >= 180 else LEFT
        turn_deg = math.fabs(180-heading)
    elif direction == SOUTH:
        turn_dir = RIGHT if heading >= 270 else LEFT
        turn_deg = math.fabs(270-heading)
    dt.turn_for(turn_dir, turn_deg)


# Hàm hỗ trợ di chuyển
def move_to_coord(current_coord, new_coord):
    current_row, current_col = current_coord
    new_row, new_col = new_coord

    row_diff = new_row - current_row
    col_diff = new_col - current_col

    # Di chuyen theo truc doc
    if row_diff != 0:
        if row_diff > 0:   # move one grid south
            turn_to(SOUTH)
            move_one_grid()
        else:   # move north
            turn_to(NORTH)
            move_one_grid()
    # Di chuyen theo truc ngang
    elif col_diff != 0:
        if col_diff > 0:   # move east
            turn_to(EAST)
            move_one_grid()
        else:   # move west
            turn_to(WEST)
            move_one_grid()


# Hàm ứng dụng DFS để tìm ra đường đi đến đích từ một toạ độ bắt đầu
# (starting_coord)
# "coord" là viết tắt của "coordinate", tức toạ độ
def dfs(maze, starting_coord):
    # số dòng và cột của ma trận (bản đồ bản số hoá)
    n_row, n_col = len(maze), len(maze[0])

    path = []   # stack, đường đi từ điểm khởi đầu -> đích đến
    visited = {}   # dictionary để ghi lại những toạ độ đã đi qua

    # 4 tọa độ tương đối của 4 ô trên, dưới, trái, phải so với ô hiện tại
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    # Do robot đã ở vị trí bắt đầu, đánh dấu vị trí này là "đã đi qua"
    visited[starting_coord] = 1

    # Tạo 2 biến dòng và cột, khởi tạo với giá trị là điểm khởi đầu
    current_row, current_col = starting_coord

    while True:
        is_way_found = False

        # Nhìn 4 hướng trên/dưới/trái/phải so với vị trí hiện tại,
        # và tìm đường đi được
        for direction in directions:
            # new_row, new_col là toạ độ của các ô xung quanh ô hiện tại
            new_row = current_row + direction[0]
            new_col = current_col + direction[1]

            # Bỏ qua nếu toạ độ không hợp lệ
            if new_row < 0 or new_row == n_row or \
                    new_col < 0 or new_col == n_col:
                # continue là lệnh bỏ qua vòng lặp này,
                # tiếp tục đi đến vòng lặp tiếp theo
                continue

            new_coord = (new_row, new_col)

            # Tra cứu giá trị của toạ độ mới trong bản đồ
            # xem đây có phải là đường đi được không và đã đi qua chưa
            # if x in [1,2,3]
            # --> tuong duong: x == 1 or x == 2 or x == 3
            if maze[new_row][new_col] in OPEN_CODES and \
                    new_coord not in visited:
                is_way_found = True
                path.append((current_row, current_col))

                # Nếu giá trị của ô trong ma trận là 3 thì đã tìm được đường đi
                if maze[new_row][new_col] == DESTINATION_CODE:
                    print("Da tim duoc duong di!")
                    path.append(new_coord)
                    return path

                # Do toạ độ mới này đi được, ta sẽ di chuyển tới ô
                current_row, current_col = new_coord
                # Ghi lại là ta đã đi qua ô này
                visited[(current_row, current_col)] = 1
                # Ngừng vòng lặp 4 (nhìn 4 hướng) để đi tiếp vào ô đã chọn
                break

        # Nếu không tìm được đường đi,
        # ta đi ngược lại và lấy toạ độ vừa đi ngược ra khỏi stack
        if not is_way_found:
            current_row, current_col = path.pop()

        # Nếu đi hết bản đồ mà vẫn không tìm được đích đến, thoát chương trình
        if len(path) == 0:
            print("Khong tim duoc duong di.")

    return path


def follow_path(path):
    current_coord = path[0]
    remaining_path = path[1:]

    for new_coord in remaining_path:
        move_to_coord(current_coord, new_coord)
        current_coord = new_coord


# CHƯƠNG TRÌNH CHÍNH
# ==================

dt.set_drive_velocity(60)   # percent
dt.set_turn_velocity(50)   # percent
gyro.start_calibration()   # cam bien phuong huong
gyro.set_heading(0)

MAZE = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
]


START_COORD = (1, 4)
solution_path = dfs(MAZE, START_COORD)

print(solution_path)

follow_path(solution_path)
