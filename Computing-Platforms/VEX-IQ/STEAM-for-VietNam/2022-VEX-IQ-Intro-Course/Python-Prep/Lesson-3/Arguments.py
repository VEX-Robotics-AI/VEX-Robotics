"""
http://bit.ly/S4V_CS201_Arguments
https://www.robotmesh.com/studio/60cc04235ba6e20556d8a383

Cách sửa lỗi sau khi Copy Project:
Xoá tất cả nội dung trong các dòng từ
#region config
đến
#endregion config
"""


# IMPORT CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ================================
import sys

from vex import (
    Motor,
    Touchled,
    Ports,
    DistanceUnits,
    ColorHue
)
from vex import (FORWARD, RIGHT, LEFT)
from drivetrain import Drivetrain


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================
# khởi tạo các motor, cắm vào cổng 1 & 2 của Brain (bộ xử lý trung tâm)
motor_right = Motor(Ports.PORT1, True)   # Reverse Polarity
motor_left = Motor(Ports.PORT2)

# === THỰC HÀNH THAM SỐ CỦA HÀM ===
# Lưu ý: Chỉ nhận tham số theo vị trí
# phương thức khởi tạo của bộ truyền động
# def __init__(self, left_motor, right_motor, wheel_travel=200,
#              track_width=176, distanceUnits=DistanceUnits.MM, gear_ratio=1.0)

# thiếu tham số bắt buộc
# drivetrain   = Drivetrain(motor_left)

# chỉ có tham số bắt buộc
# không báo lỗi nhưng hoạt động không đúng
# drivetrain   = Drivetrain(motor_left, motor_right)

# tham số đặt sai vị trí
# không báo lỗi nhưng hoạt động không đúng
# drivetrain = Drivetrain(motor_left, motor_right, DistanceUnits.MM)

# đủ tham số bắt buộc
# tham số không bắt buộc truyền đúng vị trí
# chương trình hoạt động đúng
# drivetrain = Drivetrain(
#     motor_left, motor_right,
#     200, 202, DistanceUnits.MM
# )

# truyền đầy đủ tham số đúng vị trí
# chương trình hoạt động đúng
# khởi tạo drivetrain (bộ truyền động) với 2 motor
# mỗi motor gắn một bánh xe chu vi 200mm
# và khoảng cách giữa 2 bánh xe 2 bên là 202mm
# tỉ lệ bánh răng 1:1
drivetrain = Drivetrain(
    motor_left, motor_right,
    200, 202, DistanceUnits.MM, 1
)

# ================================

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
        flash_led(ColorHue.RED, 0.3)   # goi ham flash_led o phia tren


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
