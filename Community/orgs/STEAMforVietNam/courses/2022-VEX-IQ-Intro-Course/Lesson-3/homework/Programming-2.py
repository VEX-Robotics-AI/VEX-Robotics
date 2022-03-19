"""
Lập trình cho robot sao cho mỗi lần bấm bumper,
đèn TouchLED sẽ bật sáng màu bất kỳ trong 1 giây.
Nếu bumper không được nhấn thì đèn TouchLED sẽ bị tắt.
"""


# NHẬP CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ==============================

from vex import Ports, Bumper, Touchled, ColorHue
from random import randint
import sys


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo sensor
bumper = Bumper(Ports.PORT5)
touch_led = Touchled(Ports.PORT10)


# ĐỊNH NGHĨA CÁC HÀM
# ==================

# Học sinh sẽ phải lập trình cho hàm operate() sau đây
# để thực hiện yêu cầu đề bài
def operate():
    # Nếu bumper được bấm
    if bumper.pressing():
        # Bật đèn LED màu ngẫu nhiên
        touch_led.on_hue(randint(ColorHue.RED, ColorHue.WHITE))

        # Đợi trong 1 giây
        sys.sleep(1)

        # Tắt đèn LED
        touch_led.off()


# CHƯƠNG TRÌNH CHÍNH
# ==================

while True:
    operate()
