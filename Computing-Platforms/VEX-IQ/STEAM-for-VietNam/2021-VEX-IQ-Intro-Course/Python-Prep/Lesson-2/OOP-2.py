"""
http://bit.ly/S4V_CS201_OOP2
https://www.robotmesh.com/studio/60bd5d655ba6e20556d7ed3a
"""


import random
import sys

from vex import (Ports, Touchled, ColorHue)


touch_led = Touchled(Ports.PORT1)


# Thử tính năng chạm cảm ứng của "đối tượng" Touch LED
# ====================================================
def test_pressing_led():
    times = 0
    while True:
        if touch_led.pressing():   # True/False
            times += 1
            print("Ui da! Cham vao tui " + str(times) + " lan roi nha!")
            sys.sleep(0.1)

# test_pressing_led()


# Thử tính năng đổi màu của Touch LED
# ====================================================
COLORS = [ColorHue.WHITE, ColorHue.GREEN, ColorHue.RED, ColorHue.VIOLET]


def get_random_color():
    random_index = random.randint(0, len(COLORS) - 1)   # random integer
    return COLORS[random_index]


def test_changing_led_color():
    while True:
        if touch_led.pressing():
            color = get_random_color()
            touch_led.on_hue(color)   # phuong thuc on_hue(thamso)
            sys.sleep(0.5)


test_changing_led_color()
