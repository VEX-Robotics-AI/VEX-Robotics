"""
Unit Test này cần Controller được kết nối với Brain

On Robot Mesh Studio: https://www.robotmesh.com/studio/60112e84bf4a15058c6bbeb0
"""


# NHẬP CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ==============================

from vex import (
    Brain, Controller
)


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo brain
brain = Brain()

# khởi tạo bộ điều khiển từ xa
ctl = Controller()


# CHƯƠNG TRÌNH CHÍNH
# ==================

while True:
    # in ra màn hình phím Controller nào đang được bấm, hoặc
    # in ra giá trị số đo các trục Joystick A, B, C, D
    if ctl.buttonEUp.pressing():
        brain.screen.print_line(1, 'E Up')

    elif ctl.buttonEDown.pressing():
        brain.screen.print_line(1, 'E Down')

    elif ctl.buttonFUp.pressing():
        brain.screen.print_line(1, 'F Up')

    elif ctl.buttonFDown.pressing():
        brain.screen.print_line(1, 'F Down')

    elif ctl.buttonLUp.pressing():
        brain.screen.print_line(1, 'L Up')

    elif ctl.buttonLDown.pressing():
        brain.screen.print_line(1, 'L Down')

    elif ctl.buttonRUp.pressing():
        brain.screen.print_line(1, 'R Up')

    elif ctl.buttonRDown.pressing():
        brain.screen.print_line(1, 'R Down')

    else:
        brain.screen.print_line(
            1,
            'A=' + str(ctl.axisA.position()) + ', ' +
            'B=' + str(ctl.axisB.position())
        )
        brain.screen.print_line(
            2,
            'C=' + str(ctl.axisC.position()) + ', ' +
            'D=' + str(ctl.axisD.position())
        )

    brain.screen.clear_screen()
