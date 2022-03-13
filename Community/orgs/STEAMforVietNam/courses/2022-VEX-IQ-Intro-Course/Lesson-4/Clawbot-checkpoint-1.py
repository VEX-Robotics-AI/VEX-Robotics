"""
On Robot Mesh Studio: https://www.robotmesh.com/studio/600c5a1f7ec24d0652034da5
"""


# NHẬP CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ==============================

from vex import (
    Brain, Controller, Motor,
    Ports, BrakeType, FORWARD, PERCENT, REVERSE, SECONDS
)


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo brain
brain = Brain()

# khởi tạo bộ điều khiển từ xa
ctl = Controller()
# nếu joystick không di chuyển hơn 3% thì coi như joystick không di chuyển
ctl.set_deadband(3)

# khởi tạo các motor truyền động bánh xe
left_motor = Motor(Ports.PORT1)   # motor bên trái
right_motor = Motor(Ports.PORT6, True)   # motor bên phải, quay chiều ngược lại

# khởi tạo motor cánh tay
arm_motor = Motor(Ports.PORT10)

# khởi tạo motor gọng kìm
claw_motor = Motor(Ports.PORT11)
# *** đặt TIMEOUT cho motor gọng kìm để tránh việc motor bị nghẽn ***
# ...


# ĐỊNH NGHĨA CÁC HÀM
# ==================

# điều khiển cánh tay
def lower_or_raise_arm_by_controller(arm_motor_velocity_percent=100):
    # hạ cánh tay bằng phím L Xuống hoặc R Xuống
    if ctl.buttonLDown.pressing() or ctl.buttonRDown.pressing():
        arm_motor.spin(REVERSE, arm_motor_velocity_percent, PERCENT)

    # nâng cánh tay bằng phím L Lên hoặc R Lên
    elif ctl.buttonLUp.pressing() or ctl.buttonRUp.pressing():
        arm_motor.spin(FORWARD, arm_motor_velocity_percent, PERCENT)

    else:
        arm_motor.stop(BrakeType.HOLD)


# điều khiển gọng kìm
def close_or_open_claw_by_controller(claw_motor_velocity_percent=100):
    # mở gọng kìm bằng phím E Xuống

    # đóng gọng kìm bằng phím E Lên

    pass


# lái 2 bánh xe bằng 2 joystick (A + D) của bộ điều khiển từ xa
def drive_by_controller():
    # lái bánh xe bên trái bằng joystick A

    # lái bánh xe bên phải bằng joystick D

    pass


# CHƯƠNG TRÌNH CHÍNH
# ==================

while True:
    lower_or_raise_arm_by_controller()
