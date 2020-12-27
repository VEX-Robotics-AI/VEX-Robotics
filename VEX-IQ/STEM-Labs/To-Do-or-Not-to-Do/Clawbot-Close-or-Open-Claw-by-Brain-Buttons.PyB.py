from vex import Brain, BrakeType, DirectionType, Motor, Ports, VelocityUnits


class Clawbot:
    CLAW_MOTOR_PORT = Ports.PORT11
    CLAW_MOTOR_REVERSE_POLARITY = False

    def __init__(self):
        self.brain = Brain()

        self.claw_motor = \
            Motor(
                self.CLAW_MOTOR_PORT,   # index
                self.CLAW_MOTOR_REVERSE_POLARITY   # reverse
            )


CLAWBOT = Clawbot()


while True:
    if CLAWBOT.brain.buttonUp.pressing():
        CLAWBOT.claw_motor.spin(
            DirectionType.FWD,   # dir
            None,   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

    elif CLAWBOT.brain.buttonDown.pressing():
        CLAWBOT.claw_motor.spin(
            DirectionType.REV,   # dir
            None,   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

    else:
        CLAWBOT.claw_motor.stop(BrakeType.HOLD)
