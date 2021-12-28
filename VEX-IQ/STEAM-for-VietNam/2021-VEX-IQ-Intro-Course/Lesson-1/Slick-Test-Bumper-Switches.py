"""
Unit Test này yêu cầu mô hình Slick có gắn thêm Motors & Sensors

On Robot Mesh Studio: https://www.robotmesh.com/studio/5ffe5199ce773b05bc962da4
"""


# NHẬP CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ==============================

from vex import (
    Brain, Bumper,
    Ports, SECONDS
)
from random import randint


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo brain
brain = Brain()

# khởi tạo các bumper switch
bumper_9 = Bumper(Ports.PORT9)
bumper_10 = Bumper(Ports.PORT10)


# CHƯƠNG TRÌNH CHÍNH
# ==================

while True:
    # mỗi khi một trong những bumper switches được nhấn
    # thì brain phát âm thanh ngẫu nhiên
    if bumper_9.pressing() or bumper_10.pressing():
        brain.sound.play(
            randint(1, 7),   # note: một trong 7 note C, D, E, F, G, A, B
            randint(1, 7),   # octave: một số từ 1 đến 7
            0.5, SECONDS   # 0.5 giây
        )
