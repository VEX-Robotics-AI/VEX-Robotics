"""
Lập trình cho robot liên tục di chuyển từng bước 10mm một (tốc độ 100%),
khi robot cách vật cản 200mm hay thấp hơn thì đèn TouchLED bật màu cam,
sau đó robot tiếp tục di chuyển đến khi cách vật cản 50mm hay thấp hơn
thì đèn TouchLED chuyển sang màu đỏ và ngừng chạy.
"""


from vex import (
    Motor, Ports, DEGREES, FORWARD, MM, PERCENT,
    Touchled, ColorHue, Sonar
)
import sys
from drivetrain import Drivetrain


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo các motor
motor_right = Motor(Ports.PORT1, True)  # reverse=True: đảo ngược chiều xoay
motor_left = Motor(Ports.PORT2)

# khởi tạo sensor
touch_led = Touchled(Ports.PORT10)
distance_sensor = Sonar(Ports.PORT7)

# khởi tạo drivetrain với 2 motor, mỗi motor gắn một bánh xe
# chu vi 200mm và khoảng cách giữa 2 bánh xe 2 bên là 176mm
dt = Drivetrain(motor_left, motor_right, 200, 176)


# Học sinh sẽ phải lập trình cho hàm operate() sau đây để thực hiện yêu cầu đề bài
def operate():
    ...


# Chương trình chính
while True:
    operate()
