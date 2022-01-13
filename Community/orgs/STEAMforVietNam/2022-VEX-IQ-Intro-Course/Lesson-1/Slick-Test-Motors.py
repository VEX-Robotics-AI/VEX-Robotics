"""
Unit Test này yêu cầu mô hình Slick có gắn thêm Motors & Sensors

On Robot Mesh Studio: https://www.robotmesh.com/studio/5ffe521a7ec24d06520134c2
"""


# NHẬP CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ==============================

from vex import (
    Motor,
    Ports, DEGREES, FORWARD, PERCENT, REVERSE
)


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo các motor
motor_1 = Motor(Ports.PORT1, True)   # reverse: đảo ngược chiều xoay mặc định
motor_6 = Motor(Ports.PORT6)
motor_7 = Motor(Ports.PORT7, True)   # reverse: đảo ngược chiều xoay mặc định
motor_12 = Motor(Ports.PORT12)


# CHƯƠNG TRÌNH CHÍNH
# ==================

# lần lượt quay các motor
for motor in [motor_1, motor_6, motor_7, motor_12]:
    motor.spin_for(
        FORWARD,   # quay theo chiều xuôi
        360, DEGREES,   # 360 độ (1 vòng)
        100, PERCENT,   # tốc độ (velocity) 100%
        True   # waitForCompletion: chờ chạy xong bước này mới bắt đầu bước sau
    )
    motor.spin_for(
        REVERSE,   # quay theo chiều ngược lại
        360, DEGREES,   # 360 độ (1 vòng)
        100, PERCENT,   # tốc độ (velocity) 100%
        True   # waitForCompletion: chờ chạy xong bước này mới bắt đầu bước sau
    )
