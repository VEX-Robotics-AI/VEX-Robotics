from drivetrain import Drivetrain
from vex import \
    DirectionType, \
    DistanceUnits, \
    Motor, \
    Ports, \
    RotationUnits, \
    TimeUnits, \
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
    ARM_MOTOR_VELOCITY = 30   # %

    CLAW_MOTOR_PORT = Ports.PORT11
    CLAW_MOTOR_REVERSE_POLARITY = False
    CLAW_MOTOR_TIMEOUT_SECS = 3
    CLAW_MOTOR_VELOCITY = 60   # %

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
        self.claw_motor.set_timeout(
            self.CLAW_MOTOR_TIMEOUT_SECS,   # time
            TimeUnits.SEC   # timeUnit
        )


if __name__ == 'TBD':
    CLAWBOT = Clawbot()

    # open the Claw 75 degrees
    CLAWBOT.claw_motor.spin_for(
        DirectionType.REV,   # dir
        75,   # rotation
        RotationUnits.DEG,   # rotationUnit
        None,   # velocity
        VelocityUnits.PCT,   # velocityUnit
        True   # waitForCompletion
    )

    # drive forward 150 mm to approach the object
    CLAWBOT.drivetrain.drive_for(
        DirectionType.FWD,   # directionType
        150,   # distance
        DistanceUnits.MM,   # distanceUnit
        None,   # velocity
        VelocityUnits.PCT,   # velocityUnit
        True   # waitForCompletion
    )

    # close the Claw 60 degrees to grab the object
    CLAWBOT.claw_motor.spin_for(
        DirectionType.FWD,   # dir
        60,   # rotation
        RotationUnits.DEG,   # rotationUnit
        None,   # velocity
        VelocityUnits.PCT,   # velocityUnit
        True   # waitForCompletion
    )

    # raise the Arm 315 degrees to lift the object
    CLAWBOT.arm_motor.spin_for(
        DirectionType.FWD,   # dir
        315,   # rotation
        RotationUnits.DEG,   # rotationUnit
        None,   # velocity
        VelocityUnits.PCT,   # velocityUnit
        True   # waitForCompletion
    )

    # drive in reverse 150 mm to move the object to a new location
    CLAWBOT.drivetrain.drive_for(
        DirectionType.REV,   # directionType
        150,   # distance
        DistanceUnits.MM,   # distanceUnit
        None,   # velocity
        VelocityUnits.PCT,   # velocityUnit
        True   # waitForCompletion
    )

    # lower the Arm 315 degrees to place the object back down
    CLAWBOT.arm_motor.spin_for(
        DirectionType.REV,   # dir
        315,   # rotation
        RotationUnits.DEG,   # rotationUnit
        None,   # velocity
        VelocityUnits.PCT,   # velocityUnit
        True   # waitForCompletion
    )

    # open the Claw 60 degrees to release the object
    CLAWBOT.claw_motor.spin_for(
        DirectionType.REV,   # dir
        60,   # rotation
        RotationUnits.DEG,   # rotationUnit
        None,   # velocity
        VelocityUnits.PCT,   # velocityUnit
        True   # waitForCompletion
    )
