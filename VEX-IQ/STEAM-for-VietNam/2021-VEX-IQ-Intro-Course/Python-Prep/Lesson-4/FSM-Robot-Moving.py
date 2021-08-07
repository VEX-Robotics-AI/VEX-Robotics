"""
https://bit.ly/S4V_CS201_FSM_Robot_Moving
https://www.robotmesh.com/studio/60e81e9ec25db4502989b540

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
    Bumper,
    Ports,
    DistanceUnits,
    ColorHue
)
from vex import (FORWARD, LEFT, DEGREES)
from drivetrain import Drivetrain


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo các motor, cắm vào cổng 1 & 2 của Brain (bộ xử lý trung tâm)
motor_right = Motor(Ports.PORT1, True)   # Reverse Polarity
motor_left = Motor(Ports.PORT2)

# khởi tạo drivetrain (bộ truyền động) với 2 motor
# mỗi motor gắn một bánh xe chu vi 200mm
# và khoảng cách giữa 2 bánh xe 2 bên là 202mm
# tỉ lệ bánh răng 1:1
drivetrain = Drivetrain(
    motor_left, motor_right,
    200, 202, DistanceUnits.MM)

# khởi tạo đèn LED cảm ứng
touch_led = Touchled(Ports.PORT10)
# cảm biến va chạm phía trước
bumper_front = Bumper(Ports.PORT6)

# khởi tạo trạng thái
state = "IDLE_STATE"


# Định nghĩa các trạng thái
def idle_state():
    # Lấy biến trạng thái toàn cục
    global state

    # print "Idle state"
    drivetrain.stop()
    touch_led.on_hue(ColorHue.RED)

    while True:
        # Chuyển trạng thái khi đèn trên bấm
        if touch_led.pressing():
            state = "FORWARD_STATE"
            print("Press the touch led up")
            return


def forward_state():
    # Lấy biến trạng thái toàn cục
    global state

    print("Forward state")
    touch_led.on_hue(ColorHue.GREEN)
    drivetrain.start_drive_for(FORWARD, 50, DistanceUnits.CM, 50)

    while True:
        # Chuyển trạng thái khi chạy xong
        if drivetrain.is_done():
            state = "IDLE_STATE"
            return

        # Chuyển trạng thái khi
        # cảm biến va chạm đụng vật cản
        if bumper_front.pressing():
            state = "TURN_STATE"
            return


def turn_state():
    # Lấy biến trạng thái toàn cục
    global state
    # dừng drivetrain
    drivetrain.stop()
    # bắt đầu rẽ trái 90 độ
    drivetrain.start_turn_for(LEFT, 90, DEGREES)

    while True:
        # Chuyển trạng thái khi quay xong
        if drivetrain.is_done():
            state = "IDLE_STATE"
            return


# CHƯƠNG TRÌNH CHÍNH
# ==================
while True:
    if state == "IDLE_STATE":
        idle_state()
    elif state == "FORWARD_STATE":
        forward_state()
    elif state == "TURN_STATE":
        turn_state()
