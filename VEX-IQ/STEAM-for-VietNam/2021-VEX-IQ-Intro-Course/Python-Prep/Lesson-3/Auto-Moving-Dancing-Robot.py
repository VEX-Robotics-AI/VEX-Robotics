"""
http://bit.ly/S4V_CS201_Auto_Moving_Dancing_Robot
https://www.robotmesh.com/studio/60c641dc5ba6e20556d85fd8

Bài toán: Dùng lại bài thực hành 2,
hãy cho robot di chuyển ngẫu nhiên và mỗi khi chạm vào tường
robot sẽ lùi lại 20cm, rẽ trái 60 độ và nhảy múa,
sau đó tiếp tục di chuyển ngẫu nhiên.
"""


# IMPORT CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ================================
import sys

from vex import (
    Motor,
    Bumper,
    Touchled,
    Ports,
    DistanceUnits,
    DirectionType,
    ColorHue
)
from vex import (REVERSE, LEFT)
from drivetrain import Drivetrain


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo các motor, cắm vào cổng 1 của Brain (bộ xử lý trung tâm)
motor_right = Motor(Ports.PORT1, True)   # Reverse Polarity
motor_left = Motor(Ports.PORT2)

# khởi tạo drivetrain (bộ truyền động) với 2 motor
# mỗi motor gắn một bánh xe chu vi 200mm
# và khoảng cách giữa 2 bánh xe 2 bên là 202mm
# tỉ lệ bánh răng 1:1
drivetrain = Drivetrain(
    motor_left, motor_right,
    200, 200, DistanceUnits.MM, 1)

# khởi tạo đèn LED cảm ứng
touch_led = Touchled(Ports.PORT10)

# khởi tạo bumper trước
bumper_front = Bumper(Ports.PORT3)


# ĐỊNH NGHĨA HẰNG SỐ, THAM SỐ
# ===========================
robot_started = False
drivetrain.set_drive_velocity(100)


# ĐỊNH NGHĨA CÁC HÀM
# ==================
def flash_led(color, duration_in_seconds):
    touch_led.on_hue(color)
    sys.sleep(duration_in_seconds)


def dance():
    for _ in range(2):
        flash_led(ColorHue.YELLOW, 0.3)
        flash_led(ColorHue.RED, 0.3)


# CHƯƠNG TRÌNH CHÍNH
# ==================
# Luôn thực hiện cho đến khi bấm kết thúc chương trình
while True:
    # Robot di chuyển về phía trước
    drivetrain.drive(DirectionType.FWD)

    # Khi cảm biến va chạm được nhấn
    if bumper_front.pressing():
        # đi lùi 20 cm
        drivetrain.drive_for(REVERSE, 20, DistanceUnits.CM)
        # Robot rẽ trái 60 độ
        drivetrain.turn_for(LEFT, 120)
        # nhảy múa
        dance()
