"""
http://bit.ly/S4V_CS201_VEXIQ_API_Practice
https://www.robotmesh.com/studio/60c6c6305ba6e20556d8656c

Tham khảo VEX IQ Python API và viết chương trình
di chuyển robot đến phía trước 120cm
sau đó quay về vị trí cũ với tốc độ nhanh hơn.

LƯU Ý: Cách sửa lỗi sau khi Copy Project:
Xoá tất cả nội dung trong các dòng tự động thêm vào từ
#region config
đến
#endregion config
"""


# NẠP CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ================================
from vex import Motor, Ports
from vex import DirectionType, DistanceUnits
from drivetrain import Drivetrain


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================
# khởi tạo các motor tương ứng với các cổng
motor_left = Motor(Ports.PORT1, True)
motor_right = Motor(Ports.PORT2)

# khởi tạo bộ truyền động
drive_train = Drivetrain(motor_left, motor_right,
                         200, 192, DistanceUnits.MM, 1)


# CHƯƠNG TRÌNH CHÍNH
# ==========================
# di chuyển robot đến phía trước 120cm, tốc độ 50%
drive_train.drive_for(DirectionType.FWD, 120, DistanceUnits.CM, 50)
# di chuyển robot lui về phía sau 120cm, tốc độ 100%
drive_train.drive_for(DirectionType.REV, 120, DistanceUnits.CM, 100)
