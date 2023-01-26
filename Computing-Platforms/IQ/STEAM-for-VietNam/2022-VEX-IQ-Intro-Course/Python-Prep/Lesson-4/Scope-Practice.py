"""
https://bit.ly/S4V_CS201_FSM_Scope_Practice
https://www.robotmesh.com/studio/60e56bdfc4b0580fb15ccb96

Cách sửa lỗi sau khi Copy Project:
Xoá tất cả nội dung trong các dòng từ
#region config
...
#endregion config
"""


# IMPORT CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ================================
from vex import (
    Motor,
    Sonar,
    Ports,
    DistanceUnits
)
from vex import FORWARD, REVERSE
from drivetrain import Drivetrain


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo các motor, cắm vào cổng 1 của Brain (bộ xử lý trung tâm)
motor_right = Motor(Ports.PORT1, True)   # Reverse Polarity
motor_left = Motor(Ports.PORT2)

# khởi tạo drivetrain (bộ truyền động) với 2 motor
# mỗi motor gắn một bánh xe chu vi 200mm
# và khoảng cách giữa 2 bánh xe 2 bên là 202mm
# tỉ lệ bánh răng 1:1
drivetrain = Drivetrain(
    motor_left, motor_right,
    200, 200, DistanceUnits.MM, 1)

# Tìm đọc VEX IQ Python API cho cảm biến khoảng cách
# khởi tạo cảm biến khoảng cách
distance_front = Sonar(Ports.PORT7)


# ĐỊNH NGHĨA HẰNG SỐ, THAM SỐ
# ===========================
drivetrain.set_drive_velocity(100)
# Dòng này gây lỗi, bạn có biết nguyên nhân là gì không?
# distance_init = distance_front.distance(DistanceUnits=DistanceUnits.CM)
distance_init = distance_front.distance(DistanceUnits.CM)
print('Ban dau, robot cach tuong so CM la:', distance_init)


# CÁC HÀM
# ===========================
def get_distance_value():
    """Khoảng cách từ robot đến vật cản phía trước, đơn vị CM"""
    distance = distance_front.distance(DistanceUnits.CM)
    return distance


def get_reverse_value():
    """Khoảng cách robot cần đi lùi sau khi gặp vật cản"""
    distance = get_distance_value()
    reverse_value = distance_init - distance
    return reverse_value


# CHƯƠNG TRÌNH CHÍNH
# ==================
# Luôn thực hiện cho đến khi bấm kết thúc chương trình
while True:
    # Robot di chuyển về phía trước
    drivetrain.drive(FORWARD)

    # Khoảng cách từ robot đến vật cản phía trước
    distance_value = get_distance_value()

    # Nếu khoảng cách nhỏ hơn hoặc bằng 20 CM thì:
    if distance_value <= 20:
        # Khoảng cách robot cần đi lùi sau khi gặp vật cản
        reverse_value = get_reverse_value()
        print('Robot can di lui so CM la:', reverse_value)

        drivetrain.drive_for(REVERSE, reverse_value, DistanceUnits.CM)
        break
