from vex import \
    Brain, \
    BrakeType, \
    DirectionType, \
    Motor, \
    Ports, \
    VelocityUnits


class Clawbot:
    ARM_MOTOR_PORT = Ports.PORT10
    ARM_MOTOR_REVERSE_POLARITY = False

    CLAW_MOTOR_PORT = Ports.PORT11
    CLAW_MOTOR_REVERSE_POLARITY = False

    def __init__(self):
        self.brain = Brain()

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
        if self.brain.buttonCheck.pressing():
            self.control_arm_or_claw = 1 - self.control_arm_or_claw

    def control_arm(self):
        if not self.control_arm_or_claw:
            if self.brain.buttonUp.pressing():
                self.arm_motor.spin(
                    DirectionType.FWD,   # dir
                    100,   # velocity
                    VelocityUnits.PCT   # velocityUnit
                )

            elif self.brain.buttonDown.pressing():
                self.arm_motor.spin(
                    DirectionType.REV,   # dir
                    100,   # velocity
                    VelocityUnits.PCT   # velocityUnit
                )

            else:
                self.arm_motor.stop(BrakeType.HOLD)

        else:
            self.arm_motor.stop(BrakeType.HOLD)

    def control_claw(self):
        if self.control_arm_or_claw:
            if self.brain.buttonDown.pressing():
                self.claw_motor.spin(
                    DirectionType.REV,   # dir
                    None,   # velocity
                    VelocityUnits.PCT   # velocityUnit
                )

            elif self.brain.buttonUp.pressing():
                self.claw_motor.spin(
                    DirectionType.FWD,   # dir
                    None,   # velocity
                    VelocityUnits.PCT   # velocityUnit
                )

            else:
                self.claw_motor.stop(BrakeType.HOLD)

        else:
                self.claw_motor.stop(BrakeType.HOLD)


if __name__ == 'TBD':
    CLAWBOT = Clawbot()

    while True:
        CLAWBOT.switch_between_arm_and_claw()
        CLAWBOT.control_arm()
        CLAWBOT.control_claw()
