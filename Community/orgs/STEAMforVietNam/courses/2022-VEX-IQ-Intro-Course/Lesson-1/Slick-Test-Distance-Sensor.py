"""
Unit Test này yêu cầu mô hình Slick có gắn thêm Motors & Sensors

On Robot Mesh Studio: https://www.robotmesh.com/studio/5ffe51fe7ec24d06520134bf
"""


# NHẬP CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ==============================

from vex import (
    Brain, Sonar,
    Ports, MM, SECONDS
)
from random import randint


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo brain
brain = Brain()

# khởi tạo sensor cảm biến khoảng cách
distance_sensor = Sonar(Ports.PORT4)


# CHƯƠNG TRÌNH CHÍNH
# ==================

while True:
    # mỗi khi có sensor cảm nhận một vật ở gần hơn 10 cm
    # thì brain phát âm thanh ngẫu nhiên
    if distance_sensor.distance(MM) < 100:
        brain.sound.play(
            randint(1, 7),   # note: một trong 7 note C, D, E, F, G, A, B
            randint(1, 7),   # octave: một số từ 1 đến 7
            0.5, SECONDS   # 0.5 giây
        )
