"""
https://bit.ly/S4V_CS201_Practice_Sonar
https://www.robotmesh.com/studio/60e482cac25db4502989a335

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
# khởi tạo các motor
motor_right = Motor(Ports.PORT1, True)
motor_left = Motor(Ports.PORT2)

# khởi tạo drivetrain (bộ truyền động) với 2 motor
# mỗi motor gắn một bánh xe chu vi 200mm
# và khoảng cách giữa 2 bánh xe 2 bên là 202mm
# tỉ lệ bánh răng 1:1
drivetrain = Drivetrain(
    motor_left, motor_right,
    200, 200, DistanceUnits.MM, 1)

# khởi tạo cảm biến khoảng cách
distance_front = Sonar(Ports.PORT7)


# ĐỊNH NGHĨA HẰNG SỐ, THAM SỐ
# ===========================
drivetrain.set_drive_velocity(100)

# Dòng này gây lỗi, bạn có biết nguyên nhân là gì không?
# distance_start = distance_front.distance(DistanceUnits=DistanceUnits.CM)
distance_start = distance_front.distance(DistanceUnits.CM)
print('Ban dau, robot cach tuong so CM la:', distance_start)


# CHƯƠNG TRÌNH CHÍNH
# ==================
while True:
    # Robot di chuyển về phía trước
    drivetrain.drive(FORWARD)

    # Khoảng cách distance cảm biến khoảng cách
    # đọc được cách vật đối diện
    distance_value = distance_front.distance(DistanceUnits.CM)
    print('Robot cach tuong so CM la:', distance_value)

    # Nếu khoảng cách nhỏ hơn hoặc bằng 20 CM thì:
    if distance_value <= 20:
        # Xác định khoảng cách cần lùi
        reverse_value = distance_start - distance_value
        print('Robot can di lui so CM la:', reverse_value)

        # Robot đi lùi
        drivetrain.drive_for(REVERSE, reverse_value, DistanceUnits.CM)

        # thoát khỏi vòng lặp while True
        # để dừng chương trình
        # sau khi về vị trí cũ
        break
