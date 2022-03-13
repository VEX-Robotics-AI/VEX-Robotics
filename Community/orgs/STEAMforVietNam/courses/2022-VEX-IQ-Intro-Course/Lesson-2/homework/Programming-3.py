"""
Hãy sử dụng drivetrain để điều khiển robot đi thẳng 100cm rồi lùi về 50 cm,
sau đó xoay phải 90 độ, cuối cùng đi thẳng 50cm rồi lùi về 50 cm.
Tốc độ di chuyển của robot là 100%, tốc độ xoay là 10%.
"""


# IMPORT CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ================================

from vex import (
    Motor, Ports,
    RIGHT, FORWARD, REVERSE, DEGREES, PERCENT, DistanceUnits
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
dt.drive_for(FORWARD, 100, DistanceUnits.CM, 100, PERCENT)
dt.drive_for(REVERSE, 50, DistanceUnits.CM, 100, PERCENT)
dt.turn_for(RIGHT, 90, DEGREES, 10, PERCENT)
dt.drive_for(FORWARD, 50, DistanceUnits.CM, 100, PERCENT)
dt.drive_for(REVERSE, 50, DistanceUnits.CM, 100, PERCENT)
