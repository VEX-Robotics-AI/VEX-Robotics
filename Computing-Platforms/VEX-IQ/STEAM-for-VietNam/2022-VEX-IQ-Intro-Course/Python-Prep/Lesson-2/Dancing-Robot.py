"""
http://bit.ly/S4V_CS201_Dancing_Robot
https://www.robotmesh.com/studio/60c0362a5ba6e20556d81961

Cách sửa lỗi sau khi Copy Project:
Xoá tất cả nội dung trong các dòng từ
#region config
đến
#endregion config
"""


# IMPORT CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ================================

from vex import (
    Motor,
    Touchled,
    Ports,
    DistanceUnits,
    ColorHue
)
from vex import (FORWARD, RIGHT, LEFT)
from drivetrain import Drivetrain
import sys


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo các motor, cắm vào cổng 1 & 2 của Brain (bộ xử lý trung tâm)
motor_right = Motor(Ports.PORT1, True)   # Reverse Polarity
motor_left = Motor(Ports.PORT2)

# khởi tạo drivetrain (bộ truyền động) với 2 motor, mỗi motor gắn một bánh xe
# chu vi 200mm và khoảng cách giữa 2 bánh xe 2 bên là 202mm
# và tỉ lệ bánh răng1:1
drivetrain = Drivetrain(motor_left, motor_right, 200, 202, DistanceUnits.MM, 1)

# khởi tạo đèn LED cảm ứng
touch_led = Touchled(Ports.PORT10)


# ĐỊNH NGHĨA HẰNG SỐ, THAM SỐ
# ===========================
robot_started = False
drivetrain.set_drive_velocity(100)   # dinh nghia toc do mac dinh cua robot


# ĐỊNH NGHĨA CÁC HÀM
# ==================
def flash_led(color, duration_in_seconds):
    touch_led.on_hue(color)
    sys.sleep(duration_in_seconds)


def dance():
    drivetrain.turn_for(LEFT, 30)   # re trai (LEFT) 90 do
    drivetrain.turn_for(RIGHT, 30)   # re phai (RIGHT) 90 do
    for _ in range(2):   # lap 2 lan
        flash_led(ColorHue.YELLOW, 0.3)   # goi ham flash_led o phia tren
        flash_led(ColorHue.RED, 0.3)    # goi ham flash_led o phia tren


def move_and_dance():
    for _ in range(4):   # lap 4 lan
        # di chuyen toi phia truoc (FORWARD) 120cm
        drivetrain.drive_for(FORWARD, 120, DistanceUnits.CM)
        # re trai (LEFT) 90 do
        drivetrain.turn_for(LEFT, 90)
        dance()   # goi ham dance() o phia tren


# CHƯƠNG TRÌNH CHÍNH
# ==================

# Ban đầu, bật đèn LED đỏ
touch_led.on_hue(ColorHue.RED)

# Chờ cho đến khi đèn LED được bấm vào mới bắt đầu chạy
while not robot_started:
    robot_started = touch_led.pressing()

# Bật đèn LED xanh để thể hiện robot đã bắt đầu hoạt động
touch_led.on_hue(ColorHue.GREEN)

# Di chuyển và "nhảy múa"
move_and_dance()
