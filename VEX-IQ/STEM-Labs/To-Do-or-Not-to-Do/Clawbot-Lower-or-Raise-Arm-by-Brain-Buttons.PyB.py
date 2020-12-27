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

    def __init__(self):
        self.brain = Brain()

        self.arm_motor = \
            Motor(
                self.ARM_MOTOR_PORT,   # index
                self.ARM_MOTOR_REVERSE_POLARITY   # reverse
            )


CLAWBOT = Clawbot()


while True:
    if CLAWBOT.brain.buttonUp.pressing():
        CLAWBOT.arm_motor.spin(
            DirectionType.FWD,   # dir
            100,   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

    elif CLAWBOT.brain.buttonDown.pressing():
        CLAWBOT.arm_motor.spin(
            DirectionType.REV,   # dir
            100,   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

    else:
        CLAWBOT.arm_motor.stop(BrakeType.HOLD)
