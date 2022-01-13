"""
TRÒ CHƠI THI PHẢN XẠ NHANH
==========================
Unit Test này yêu cầu mô hình Slick có gắn thêm Motors & Sensors

On Robot Mesh Studio: https://www.robotmesh.com/studio/600bed737ec24d06520346d1
"""


# NHẬP CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ==============================

from vex import (
    Brain, Motor, Bumper, Colorsensor, Gyro, Sonar, Touchled,
    Ports, FadeType, DEGREES, MM
)
from random import randint
from timer import Timer


# CÁC HẰNG SỐ
# ===========

# thời gian chơi mỗi vòng (tính bằng giây)
PLAY_TIME_IN_SECONDS = 60


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo brain
brain = Brain()

# khởi tạo các motor
motor_1 = Motor(Ports.PORT1, True)   # reverse=True: đảo ngược chiều xoay
motor_6 = Motor(Ports.PORT6)
motor_7 = Motor(Ports.PORT7, True)   # reverse=True: đảo ngược chiều xoay
motor_12 = Motor(Ports.PORT12)

# khởi tạo các bumper switch
bumper_9 = Bumper(Ports.PORT9)
bumper_10 = Bumper(Ports.PORT10)

# khởi tạo sensor cảm nhận màu sắc
color_sensor = Colorsensor(Ports.PORT2)

# sensor cảm nhận phương hướng
gyro = Gyro(Ports.PORT3)

# khởi tạo sensor cảm nhận khoảng cách
distance_sensor = Sonar(Ports.PORT4)

# khởi tạo các đèn LED cảm nhận chạm
touch_led_8 = Touchled(Ports.PORT8)
touch_led_8.brightness(100)
touch_led_8.default_fade(FadeType.OFF)

touch_led_11 = Touchled(Ports.PORT11)
touch_led_11.brightness(100)
touch_led_11.default_fade(FadeType.OFF)


# ĐỊNH NGHĨA CÁC HÀM
# ==================

# tương tác với một motor nhất định
def interact_with_motor(motor, port_number):
    brain.screen.print_line(3, 'Motor ' + str(port_number) + ': turn 60 deg!')

    # lấy vị trí quay hiện tại của motor
    current_rotation = motor.rotation(DEGREES)

    # chờ tới khi motor quay tới vị trí mới
    # lệch khỏi vị trí cũ ít nhất 60 độ
    while abs(motor.rotation(DEGREES) - current_rotation) < 60:
        pass

    brain.screen.print_line(3, 'Motor ' + str(port_number) + ' turned')


# tương tác với một bumper nhất định
def interact_with_bumper(bumper, port_number):
    brain.screen.print_line(3, 'Bumper ' + str(port_number) + ': press!')

    # chờ tới khi bumper được bấm
    while not bumper.pressing():
        pass

    brain.screen.print_line(3, 'Bumper ' + str(port_number) + ' pressed')


# tương tác với gyro ở cổng 3
def interact_with_gyro_3():
    brain.screen.print_line(3, 'Gyro 3: turn 60 deg!')

    # lấy vị trí quay hiện tại của gyro
    current_rotation = gyro.rotation(DEGREES)

    # chờ tới khi gyro quay tới vị trí mới
    # lệch khỏi vị trí cũ ít nhất 60 độ
    while abs(gyro.rotation(DEGREES) - current_rotation) < 60:
        pass

    brain.screen.print_line(3, 'Gyro 3 turned')


# tương tác với distance sensor ở cổng 4
def interact_with_distance_sensor_4():
    brain.screen.print_line(3, 'Distance Sensor 4: near!')

    # chờ tới khi có một vật lại gần distance sensor
    # trong phạm vi 10cm (100mm)
    while distance_sensor.distance(MM) > 100:
        pass

    brain.screen.print_line(3, 'Distance Sensor 4 near')


# tương tác với một touch LED nhất định
def interact_with_touch_led(touch_led, port_number):
    brain.screen.print_line(3, 'TouchLED ' + str(port_number) + ': press!')

    # nhấp nháy một màu ngẫu nhiên
    touch_led.blink_hue(randint(1, 13))

    # chờ tới khi touch LED được chạm vào
    while not touch_led.pressing():
        pass

    brain.screen.print_line(3, 'TouchLED ' + str(port_number) + ' pressed')

    # tắt đèn LED
    touch_led.off()


# CHƯƠNG TRÌNH CHÍNH
# ==================

while True:
    # điểm số bắt đầu từ 0
    score = 0

    # tạo và kích hoạt đồng hồ tính giờ
    timer = Timer()
    timer.start()

    # bắt đầu chơi
    elapsed_time = 0

    while elapsed_time <= PLAY_TIME_IN_SECONDS:
        brain.screen.print_line(
            1,
            'Score: ' + str(score) + ', ' +
            'Time: ' + str(elapsed_time)
        )

        # chơi âm thanh ngẫu nhiên trong lúc trò chơi diễn ra
        brain.sound.play_wave(randint(0, 15))

        scenario = randint(1, 12)

        if scenario == 1:
            interact_with_motor(motor_1, 1)

        elif scenario == 3:
            interact_with_gyro_3()

        elif scenario == 4:
            interact_with_distance_sensor_4()

        elif scenario == 6:
            interact_with_motor(motor_6, 6)

        elif scenario == 7:
            interact_with_motor(motor_7, 7)

        elif scenario == 8:
            interact_with_touch_led(touch_led_8, 8)

        elif scenario == 9:
            interact_with_bumper(bumper_9, 9)

        elif scenario == 10:
            interact_with_bumper(bumper_10, 10)

        elif scenario == 11:
            interact_with_touch_led(touch_led_11, 11)

        elif scenario == 12:
            interact_with_motor(motor_12, 12)

        elapsed_time = timer.elapsed_time()
        if elapsed_time <= PLAY_TIME_IN_SECONDS:
            score += 1

    brain.screen.print_line(3, 'Press CHECK to Replay...')
    while not brain.buttonCheck.pressing():
        pass
