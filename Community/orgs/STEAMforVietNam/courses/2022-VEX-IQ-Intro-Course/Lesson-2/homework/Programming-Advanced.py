"""
Hãy sử dụng drivetrain để điều khiển robot đi theo một hình tam giác đều
với cạnh 50cm rồi quay lại vị trí ban đầu. Khi di chuyển, robot chỉ xoay phải.
Tốc độ di chuyển và xoay của robot đều là 50%.

Hình dưới đây mô tả vị trí khi xuất phát & kết thúc của robot,
cũng như đường đi được yêu cầu:
"""


# IMPORT CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ================================

from vex import (
    Motor, Ports,
    LEFT, RIGHT, FORWARD, REVERSE, DEGREES, PERCENT, DistanceUnits
)
from drivetrain import Drivetrain


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo các motor
motor_left = Motor(Ports.PORT1, True)
motor_right = Motor(Ports.PORT2)   # reverse=True: đảo ngược chiều xoay

# khởi tạo drivetrain với 2 motor, mỗi motor gắn một bánh xe
# chu vi 200mm và khoảng cách giữa 2 bánh xe 2 bên là 176mm
dt = Drivetrain(motor_left, motor_right, 200, 176)

# Học sinh lập trình theo yêu cầu đề bài ở phần dưới đây:
