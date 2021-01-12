from drivetrain import Drivetrain
from vex import \
    Brain, \
    DirectionType, \
    DistanceUnits, \
    Motor, \
    Ports, \
    RotationUnits, \
    TimeUnits, \
    Touchled, \
    TurnType, \
    VelocityUnits

from random import randint


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

    # sensor configs
    TOUCH_LED_PORT = Ports.PORT2

    # actuator configs
    ARM_MOTOR_PORT = Ports.PORT10
    ARM_MOTOR_REVERSE_POLARITY = False

    CLAW_MOTOR_PORT = Ports.PORT11
    CLAW_MOTOR_REVERSE_POLARITY = False

    def __init__(self):
        self.brain = Brain()

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

        self.touch_led = Touchled(self.TOUCH_LED_PORT)

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

    # Have your Clawbot drive in a square.
    # Before each turn:
    # - The claw must be opened and closed.
    # - The arm must be raised and lowered.
    # - The Touch LED must show at least one color.
    # - At least one sound must play.
    # The Clawbot cannot drive along a side of the square more than once.
    for _ in range(4):
        CLAWBOT.drivetrain.drive_for(
            DirectionType.FWD,   # directionType
            300,   # distance
            DistanceUnits.MM,   # distanceUnit
            100,   # velocity
            VelocityUnits.PCT,   # velocityUnit
            True   # waitForCompletion
        )

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

        CLAWBOT.arm_motor.spin_for(
            DirectionType.FWD,   # dir
            900,   # rotation
            RotationUnits.DEG,   # rotationUnit
            100,   # velocity
            VelocityUnits.PCT,   # velocityUnit
            True   # waitForCompletion
        )
        CLAWBOT.arm_motor.spin_for(
            DirectionType.REV,   # dir
            900,   # rotation
            RotationUnits.DEG,   # rotationUnit
            100,   # velocity
            VelocityUnits.PCT,   # velocityUnit
            True   # waitForCompletion
        )

        CLAWBOT.touch_led.on_hue(
            randint(1, 13),   # color
            100   # brightness
        )

        CLAWBOT.brain.sound.play(
            randint(1, 7),   # note
            randint(1, 7),   # octave
            0.5,   # duration
            TimeUnits.SEC   # timeUnit
        )

        CLAWBOT.drivetrain.turn_for(
            TurnType.RIGHT,   # turnType
            90,   # angle
            RotationUnits.DEG,   # rotationUnit
            100,   # velocity
            VelocityUnits.PCT,   # velocityUnit
            True   # waitForCompletion
        )
