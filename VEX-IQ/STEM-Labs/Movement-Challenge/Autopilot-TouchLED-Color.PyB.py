from vex import ColorHue, Ports, Touchled


class Autopilot:
    TOUCH_LED_PORT = Ports.PORT2

    def __init__(self):
        self.touch_led = Touchled(self.TOUCH_LED_PORT)


AUTOPILOT = Autopilot()


AUTOPILOT.touch_led.on_hue(
    ColorHue.GREEN,   # color
    100   # brightness
)
