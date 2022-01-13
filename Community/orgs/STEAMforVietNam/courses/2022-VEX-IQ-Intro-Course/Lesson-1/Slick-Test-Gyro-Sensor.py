"""
Unit Test này yêu cầu mô hình Slick có gắn thêm Motors & Sensors

On Robot Mesh Studio: https://www.robotmesh.com/studio/5ffe51b97ec24d06520134b8
"""


# NHẬP CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ==============================

from vex import (
    Brain, Gyro,
    Ports, GyroCalibrationType, DEGREES
)


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo brain
brain = Brain()

# khởi tạo sensor cảm nhận phương hướng
gyro_sensor = Gyro(Ports.PORT3)


# CHƯƠNG TRÌNH CHÍNH
# ==================

# calibrate sensor cảm nhận phương hướng
brain.screen.print_line(
    1,
    'Calibrating Gyro...'
)
gyro_sensor.start_calibration(
    GyroCalibrationType.ACCURATE,   # QUICK, SLOW hoặc ACCURATE
    True   # chờ calibrate xong hẳn
)

while True:
    # in ra màn hình của brain
    # các số đo Heading và Rotation của sensor cảm nhận phương hướng
    brain.screen.print_line(
        1,
        'Heading: ' + str(int(gyro_sensor.heading(DEGREES)))
    )
    brain.screen.print_line(
        2,
        'Rotation: ' + str(int(gyro_sensor.rotation(DEGREES)))
    )
