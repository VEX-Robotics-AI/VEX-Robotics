"""
Lập trình cho đèn TouchLED nhấp nháy liên tục với chu kỳ
3 giây đèn sáng màu đỏ, 1 giây đèn sáng màu vàng.
"""


from vex import Ports, Touchled, ColorHue


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo sensor
touch_led = Touchled(Ports.PORT10)


# Học sinh sẽ phải lập trình cho hàm operate() sau đây để điều khiển TouchLED thực hiện yêu cầu đề bài
def operate():
    ...


# Chương trình chính
while True:
    operate()
