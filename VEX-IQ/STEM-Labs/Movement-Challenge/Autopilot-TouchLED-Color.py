from vexiq import NamedColor, TouchLed


class Autopilot:
    TOUCH_LED_PORT = 2

    def __init__(self):
        self.touch_led = TouchLed(self.TOUCH_LED_PORT)


if __name__ == 'TBD':
    AUTOPILOT = Autopilot()

    # AUTOPILOT.touch_led.color(
    #     0,   # red
    #     100,   # green
    #     0,   # blue
    #     100   # brightness
    # )
    AUTOPILOT.touch_led.named_color(NamedColor.GREEN)
    AUTOPILOT.touch_led.on()
