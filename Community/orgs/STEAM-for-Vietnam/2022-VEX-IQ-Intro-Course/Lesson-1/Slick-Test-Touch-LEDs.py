"""
Unit Test này yêu cầu mô hình Slick có gắn thêm Motors & Sensors

On Robot Mesh Studio: https://www.robotmesh.com/studio/5ffe52317ec24d06520134c7
"""


# NHẬP CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ==============================

from vex import (
    Touchled,
    Ports, FadeType,
    wait
)
from random import randint


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo các đèn LED cảm biến va chạm
touch_led_8 = Touchled(Ports.PORT8)
touch_led_8.brightness(100)
touch_led_8.default_fade(FadeType.FAST)

touch_led_11 = Touchled(Ports.PORT11)
touch_led_11.brightness(100)
touch_led_11.default_fade(FadeType.FAST)


# ĐỊNH NGHĨA CÁC HÀM
# ==================

def turn_led_on_if_touched(touch_led):
    # nếu touch_led  được nhấn thì touch_led đó nhấp nháy 1 giây
    if touch_led.pressing():
        touch_led.blink_hue(
            randint(1, 13),   # một trong 13 màu trong ColorHue
            0.25,   # on_time
            0.25    # off_time
        )
        wait(1)
        touch_led.off()


# CHƯƠNG TRÌNH CHÍNH
# ==================

while True:
    turn_led_on_if_touched(touch_led_8)
    turn_led_on_if_touched(touch_led_11)
