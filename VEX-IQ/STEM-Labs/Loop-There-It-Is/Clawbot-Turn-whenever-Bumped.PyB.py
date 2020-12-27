from drivetrain import Drivetrain
from vex import \
    Bumper, \
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

    # sensor configs
    BUMPER_SWITCH_PORT = Ports.PORT8

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

        self.bumper_switch = Bumper(self.BUMPER_SWITCH_PORT)


CLAWBOT = Clawbot()


while True:
    if CLAWBOT.bumper_switch.pressing():
        CLAWBOT.drivetrain.turn_for(
            TurnType.RIGHT,   # turnType
            90,   # angle
            RotationUnits.DEG,   # rotationUnits
            None,   # velocity
            VelocityUnits.PCT,   # velocityUnits
            True   # waitForCompletion
        )

    else:
        CLAWBOT.drivetrain.drive(
            DirectionType.FWD,   # directionType
            None,   # velocity
            VelocityUnits.PCT   # velocityUnits
        )
