"""
Lập trình cho đèn TouchLED nhấp nháy liên tục với chu kỳ
3 giây đèn sáng màu đỏ, 1 giây đèn sáng màu vàng.
"""


# NHẬP CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ==============================

from vex import Ports, Touchled, ColorHue
import sys


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo sensor
touch_led = Touchled(Ports.PORT10)


# ĐỊNH NGHĨA CÁC HÀM
# ==================

# Học sinh sẽ phải lập trình cho hàm operate() sau đây
# để điều khiển TouchLED thực hiện yêu cầu đề bài
def operate():
    # Bật đèn LED màu đỏ
    touch_led.on_hue(ColorHue.RED)
    # Đợi trong 3 giây
    sys.sleep(3)

    # Bật đèn LED màu vàng
    touch_led.on_hue(ColorHue.YELLOW)
    # Đợi trong 1 giây
    sys.sleep(1)

    # Tắt đèn LED
    touch_led.off()


# CHƯƠNG TRÌNH CHÍNH
# ==================

while True:
    operate()
