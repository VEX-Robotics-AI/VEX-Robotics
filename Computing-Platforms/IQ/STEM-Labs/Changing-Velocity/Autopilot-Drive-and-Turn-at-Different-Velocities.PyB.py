from drivetrain import Drivetrain
from vex import \
    DirectionType, \
    DistanceUnits, \
    Motor, \
    Ports, \
    RotationUnits, \
    TurnType, \
    VelocityUnits


class Autopilot:
    # drive base configs
    LEFT_MOTOR_PORT = Ports.PORT1
    LEFT_MOTOR_REVERSE_POLARITY = False

    RIGHT_MOTOR_PORT = Ports.PORT6
    RIGHT_MOTOR_REVERSE_POLARITY = True

    WHEEL_TRAVEL = 200
    TRACK_WIDTH = 176
    DISTANCE_UNIT = DistanceUnits.MM
    GEAR_RATIO = 1

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


AUTOPILOT = Autopilot()


AUTOPILOT.drivetrain.drive_for(
    DirectionType.FWD,   # directionType
    5,   # distance
    DistanceUnits.IN,   # distanceUnit
    50,   # velocity
    VelocityUnits.PCT,   # velocityUnit
    True   # waitForCompletion
)

AUTOPILOT.drivetrain.turn_for(
    TurnType.RIGHT,   # turnType
    90,   # angle
    RotationUnits.DEG,   # rotationUnits
    50,   # velocity
    VelocityUnits.PCT,   # velocityUnit
    True   # waitForCompletion
)

AUTOPILOT.drivetrain.drive_for(
    DirectionType.REV,   # directionType
    5,   # distance
    DistanceUnits.IN,   # distanceUnit
    25,   # velocity
    VelocityUnits.PCT,   # velocityUnit
    True   # waitForCompletion
)

AUTOPILOT.drivetrain.turn_for(
    TurnType.LEFT,   # turnType
    90,   # angle
    RotationUnits.DEG,   # rotationUnits
    75,   # velocity
    VelocityUnits.PCT,   # velocityUnit
    True   # waitForCompletion
)

AUTOPILOT.drivetrain.drive_for(
    DirectionType.FWD,   # directionType
    5,   # distance
    DistanceUnits.IN,   # distanceUnit
    75,   # velocity
    VelocityUnits.PCT,   # velocityUnit
    True   # waitForCompletion
)

AUTOPILOT.drivetrain.turn_for(
    TurnType.RIGHT,   # turnType
    90,   # angle
    RotationUnits.DEG,   # rotationUnits
    25,   # velocity
    VelocityUnits.PCT,   # velocityUnit
    True   # waitForCompletion
)
