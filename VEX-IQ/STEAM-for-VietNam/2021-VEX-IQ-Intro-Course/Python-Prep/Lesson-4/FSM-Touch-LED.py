"""
https://bit.ly/S4V_CS201_FSM_Touch_LED
https://www.robotmesh.com/studio/60e7d942c4b0580fb15cd637
"""


# IMPORT CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ================================
import vex
from vex import Touchled, Ports, ColorHue


# KHỞI TẠO
# ================================
touch_led = Touchled(Ports.PORT1)

# LƯU Ý: state, count là biến toàn cục
# Muốn thay đổi giá trị chúng trong hàm
# cần dùng từ khóa "global"
# --------------------------------
# Ban đầu, trạng thái đèn là off
state = "OFF"
# Ban đầu, biến đếm là 0
count = 0


# CÁC HÀM
# ================================
def action_off():
    # Lấy biến toàn cục
    global state

    # trạng thái: đèn tắt
    touch_led.off()

    # chuyển đổi trạng thái
    if count == 1:
        # đổi qua trạng thái xanh
        state = "ON_GREEN"


def action_green():
    # Lấy biến toàn cục
    global state

    # trạng thái: đèn màu xanh lá
    touch_led.on_hue(ColorHue.GREEN)

    # chuyển đổi trạng thái
    if count == 2:
        # đổi qua trạng thái đỏ
        state = "ON_RED"


def action_red():
    # Lấy biến toàn cục
    global count, state

    # trạng thái: đèn màu đỏ
    touch_led.on_hue(ColorHue.RED)

    # chuyển đổi trạng thái
    if count == 3:
        # reset count
        count = 0
        # chuyển về trạng thái off
        state = "OFF"


# CHƯƠNG TRÌNH CHÍNH
# ================================
while True:
    # Khi đèn được ấn
    if touch_led.pressing():
        count += 1   # Tăng biến đếm lên 1
        vex.wait(0.2)   # Cần đợi 0.2 giây cho mỗi lần ấn đèn

    # Thực hiện các hành động tương ứng với tên trạng thái
    if state == "OFF":
        action_off()
    elif state == "ON_GREEN":
        action_green()
    elif state == "ON_RED":
        action_red()
