"""
Hãy sử dụng 2 motor motor_right và motor_left,
điều khiển robot đi thẳng tới phía trước một độ dài tương đương với chu vi
bánh xe quay 1080 độ với tốc độ 75%

Trong bài tập này, học sinh chỉ cần sử dụng hàm start_spin_for của Motor
"""


# IMPORT CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ================================

from vex import Motor, Ports, FORWARD, DEGREES, PERCENT


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================
# khởi tạo các motor
motor_right = Motor(Ports.PORT1, True)  # reverse=True: đảo ngược chiều xoay
motor_left = Motor(Ports.PORT2)

# Học sinh không cần phải sử dụng sys.sleep(), chỉ cần điều khiển 2 motor
# Học sinh lập trình theo yêu cầu đề bài ở phần dưới đây:
motor_right.start_spin_for(FORWARD, 1080, DEGREES, 75, PERCENT)
motor_left.start_spin_for(FORWARD, 1080, DEGREES, 75, PERCENT)
