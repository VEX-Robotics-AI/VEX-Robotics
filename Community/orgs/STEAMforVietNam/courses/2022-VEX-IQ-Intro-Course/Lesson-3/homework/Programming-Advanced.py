"""
Lập trình cho robot di chuyển liên tục,
nếu cảm biến khoảng cách nhìn thấy vật cản thì rẽ phải 90 độ.
Robot tiếp tục di chuyển đến khi gặp vật cản thứ 3 thì ngừng hoạt động.

Biết:
- Robot luôn di chuyển & xoay với tốc độ 100%
- Mỗi lần di chuyển robot sẽ tiến 10mm
- Khoảng cách ta sẽ quy định “nhìn thấy” vật cản là khi vật cản nằm trong
khoảng cách 100mm hay gần hơn

Chú ý: "ngừng hoạt động" nghĩa là cho phần mềm điều khiển robot hoàn thành
(thay vì chỉ ra lệnh cho robot ngừng di chuyển).
"""


# IMPORT CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ================================

from vex import (
    Motor, Ports, RIGHT, FORWARD, DEGREES, PERCENT, MM,
    Sonar
)
from drivetrain import Drivetrain


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo các motor
left_motor = Motor(Ports.PORT1,True)
right_motor = Motor(Ports.PORT2)   # reverse=True: đảo ngược chiều xoay

# khởi tạo drivetrain với 2 motor, mỗi motor gắn một bánh xe
# chu vi 200mm và khoảng cách giữa 2 bánh xe 2 bên là 176mm
dt = Drivetrain(left_motor, right_motor, 200, 176)

# khởi tạo cảm biến khoảng cách
distance_sensor = Sonar(Ports.PORT3)


# Học sinh lập trình theo yêu cầu đề bài ở phần dưới đây:
