"""
Lập trình cho robot sao cho mỗi lần bấm bumper,
đèn TouchLED sẽ bật sáng màu bất kỳ trong 1 giây.
Nếu bumper không được nhấn thì đèn TouchLED sẽ bị tắt.
"""


from vex import Ports, Bumper, Touchled, ColorHue


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo sensor
bumper = Bumper(Ports.PORT5)
touch_led = Touchled(Ports.PORT10)


# Học sinh sẽ phải lập trình cho hàm operate() sau đây để thực hiện yêu cầu đề bài
def operate():
    ...


# Chương trình chính
while True:
    operate()
