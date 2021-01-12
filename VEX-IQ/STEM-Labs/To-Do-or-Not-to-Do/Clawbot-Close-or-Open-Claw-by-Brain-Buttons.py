from vexiq import Motor, is_down_button_pressed, is_up_button_pressed


class Clawbot:
    CLAW_MOTOR_PORT = 11
    CLAW_MOTOR_REVERSE_POLARITY = False

    def __init__(self):
        self.claw_motor = \
            Motor(
                self.CLAW_MOTOR_PORT,   # index
                self.CLAW_MOTOR_REVERSE_POLARITY   # reverse
            )


if __name__ == 'TBD':
    CLAWBOT = Clawbot()

    while True:
        if is_down_button_pressed():
            CLAWBOT.claw_motor.run(
                -100,   # power,
                None,   # distance
                False   # hold
            )

        elif is_up_button_pressed():
            CLAWBOT.claw_motor.run(
                100,   # power,
                None,   # distance
                False   # hold
            )

        else:
            CLAWBOT.claw_motor.hold()
