"""
Hãy sử dụng 2 motor motor_right và motor_left,
điều khiển robot đi lùi về phía sau một độ dài tương đương 3 vòng quay bánh xe,
sau đó thẳng tới phía trước một độ dài tương đương với 5 vòng quay bánh xe
với tốc độ 100%
"""


# IMPORT CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ================================

from vex import Motor, Ports, FORWARD, REVERSE, DEGREES, PERCENT


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================
# khởi tạo các motor
motor_right = Motor(Ports.PORT1, True)  # reverse=True: đảo ngược chiều xoay
motor_left = Motor(Ports.PORT2)

# Học sinh không cần phải sử dụng sys.sleep(), chỉ cần điều khiển 2 motor
# Học sinh lập trình theo yêu cầu đề bài ở phần dưới đây:
motor_right.start_spin_for(REVERSE, 1080, DEGREES, 100, PERCENT)
motor_left.start_spin_for(REVERSE, 1080, DEGREES, 100, PERCENT)

motor_right.start_spin_for(FORWARD, 1800, DEGREES, 100, PERCENT)
motor_left.start_spin_for(FORWARD, 1800, DEGREES, 100, PERCENT)
