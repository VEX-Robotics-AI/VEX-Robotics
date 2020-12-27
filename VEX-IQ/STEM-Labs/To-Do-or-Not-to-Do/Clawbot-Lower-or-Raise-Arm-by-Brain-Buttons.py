from vexiq import Motor, is_up_button_pressed, is_down_button_pressed


class Clawbot:
    ARM_MOTOR_PORT = 10
    ARM_MOTOR_REVERSE_POLARITY = False

    def __init__(self):
        self.arm_motor = \
            Motor(
                self.ARM_MOTOR_PORT,   # index
                self.ARM_MOTOR_REVERSE_POLARITY   # reverse
            )


CLAWBOT = Clawbot()


while True:
    if is_up_button_pressed():
        CLAWBOT.arm_motor.run(
            100,   # power,
            None,   # distance
            False   # hold
        )

    elif is_down_button_pressed():
        CLAWBOT.arm_motor.run(
            -100,   # power,
            None,   # distance
            False   # hold
        )

    else:
        CLAWBOT.arm_motor.hold()
