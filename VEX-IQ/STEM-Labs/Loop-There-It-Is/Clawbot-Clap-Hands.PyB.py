from drivetrain import Drivetrain
from vex import \
    DirectionType, \
    DistanceUnits, \
    Motor, \
    Ports, \
    RotationUnits, \
    TurnType, \
    VelocityUnits


class Clawbot:
    # drive base configs
    LEFT_MOTOR_PORT = Ports.PORT1
    LEFT_MOTOR_REVERSE_POLARITY = False

    RIGHT_MOTOR_PORT = Ports.PORT6
    RIGHT_MOTOR_REVERSE_POLARITY = True

    WHEEL_TRAVEL = 200
    TRACK_WIDTH = 176
    DISTANCE_UNIT = DistanceUnits.MM
    GEAR_RATIO = 1

    # actuator configs
    ARM_MOTOR_PORT = Ports.PORT10
    ARM_MOTOR_REVERSE_POLARITY = False

    CLAW_MOTOR_PORT = Ports.PORT11
    CLAW_MOTOR_REVERSE_POLARITY = False

    def __init__(self):
        self.drivetrain = \
            Drivetrain(
                Motor(
                    self.LEFT_MOTOR_PORT,   # index
                    self.LEFT_MOTOR_REVERSE_POLARITY   # reverse
                ),   # left_motor
                Motor(
                    self.RIGHT_MOTOR_PORT,   # index
                    self.RIGHT_MOTOR_REVERSE_POLARITY   # reverse
                ),   # right_motor
                self.WHEEL_TRAVEL,   # wheel_travel
                self.TRACK_WIDTH,   # track_width
                self.DISTANCE_UNIT,   # distanceUnit
                self.GEAR_RATIO   # gear_ratio
            )

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


if __name__ == 'TBD':
    CLAWBOT = Clawbot()

    CLAWBOT.arm_motor.spin_for(
        DirectionType.FWD,   # dir
        300,   # rotation
        RotationUnits.DEG,   # rotationUnit
        100,   # velocity
        VelocityUnits.PCT,   # velocityUnit
        True   # waitForCompletion
    )

    for _ in range(10):
        CLAWBOT.drivetrain.turn_for(
            TurnType.RIGHT,   # turnType
            90,   # angle
            RotationUnits.DEG,   # rotationUnits
            100,   # velocity
            VelocityUnits.PCT,   # velocityUnit
            True   # waitForCompletion
        )

        for _ in range(2):
            CLAWBOT.claw_motor.spin_for(
                DirectionType.REV,   # dir
                90,   # rotation
                RotationUnits.DEG,   # rotationUnit
                100,   # velocity
                VelocityUnits.PCT,   # velocityUnit
                True   # waitForCompletion
            )
            CLAWBOT.claw_motor.spin_for(
                DirectionType.FWD,   # dir
                90,   # rotation
                RotationUnits.DEG,   # rotationUnit
                100,   # velocity
                VelocityUnits.PCT,   # velocityUnit
                True   # waitForCompletion
            )

        CLAWBOT.drivetrain.turn_for(
            TurnType.LEFT,   # turnType
            90,   # angle
            RotationUnits.DEG,   # rotationUnits
            100,   # velocity
            VelocityUnits.PCT,   # velocityUnit
            True   # waitForCompletion
        )

        for _ in range(2):
            CLAWBOT.claw_motor.spin_for(
                DirectionType.REV,   # dir
                90,   # rotation
                RotationUnits.DEG,   # rotationUnit
                100,   # velocity
                VelocityUnits.PCT,   # velocityUnit
                True   # waitForCompletion
            )
            CLAWBOT.claw_motor.spin_for(
                DirectionType.FWD,   # dir
                90,   # rotation
                RotationUnits.DEG,   # rotationUnit
                100,   # velocity
                VelocityUnits.PCT,   # velocityUnit
                True   # waitForCompletion
            )
