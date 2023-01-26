from vexiq import \
    Motor, \
    is_check_button_pressed, \
    is_down_button_pressed, \
    is_up_button_pressed


class Clawbot:
    ARM_MOTOR_PORT = 10
    ARM_MOTOR_REVERSE_POLARITY = False

    CLAW_MOTOR_PORT = 11
    CLAW_MOTOR_REVERSE_POLARITY = False

    def __init__(self):
        self.arm_motor = \
            Motor(
                self.ARM_MOTOR_PORT,   # index
                self.ARM_MOTOR_REVERSE_POLARITY   # reverse
            )

        self.claw_motor = \
            Motor(
                self.CLAW_MOTOR_PORT,   # index
                self.CLAW_MOTOR_REVERSE_POLARITY   # reverse
            )

        self.control_arm_or_claw = 0

    def switch_between_arm_and_claw(self):
        if is_check_button_pressed():
            self.control_arm_or_claw = 1 - self.control_arm_or_claw

    def control_arm(self):
        if not self.control_arm_or_claw:
            if is_up_button_pressed():
                self.arm_motor.run(
                    100,   # power,
                    None,   # distance
                    False   # hold
                )

            elif is_down_button_pressed():
                self.arm_motor.run(
                    -100,   # power,
                    None,   # distance
                    False   # hold
                )

            else:
                self.arm_motor.hold()

        else:
            self.arm_motor.hold()

    def control_claw(self):
        if self.control_arm_or_claw:
            if is_down_button_pressed():
                self.claw_motor.run(
                    -100,   # power,
                    None,   # distance
                    False   # hold
                )

            elif is_up_button_pressed():
                self.claw_motor.run(
                    100,   # power,
                    None,   # distance
                    False   # hold
                )

            else:
                self.claw_motor.hold()

        else:
                self.claw_motor.hold()


CLAWBOT = Clawbot()


while True:
    CLAWBOT.switch_between_arm_and_claw()
    CLAWBOT.control_arm()
    CLAWBOT.control_claw()
