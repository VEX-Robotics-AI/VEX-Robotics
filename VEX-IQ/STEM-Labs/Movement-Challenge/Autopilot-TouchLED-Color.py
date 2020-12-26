from drivetrain import Drivetrain
from vexiq import Motor, NamedColor, TouchLed


class Autopilot:
    def __init__(
            self,
            left_motor_port=1, right_motor_port=6,
            wheel_travel_mm=200, track_mm=176,
            touch_led_port=2):
        self.drivetrain = \
            Drivetrain(
                Motor(
                    left_motor_port,   # port
                    False   # switch_polarity
                ),   # left_motor
                Motor(
                    right_motor_port,   # port
                    True   # switch_polarity
                ),   # right_motor
                wheel_travel_mm,   # wheel_travel_mm
                track_mm   # track_mm
            )

        self.touch_led = TouchLed(touch_led_port)


AUTOPILOT = Autopilot()

# AUTOPILOT.touch_led.color(
#     0,   # red
#     100,   # green
#     0,   # blue
#     100   # brightness
# )
AUTOPILOT.touch_led.named_color(NamedColor.GREEN)
AUTOPILOT.touch_led.on()
