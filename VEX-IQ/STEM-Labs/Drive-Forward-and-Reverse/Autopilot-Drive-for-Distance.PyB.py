from drivetrain import Drivetrain
from vex import DirectionType, DistanceUnits, Motor, Ports, VelocityUnits


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
    10,   # distance
    DistanceUnits.IN,   # distanceUnit
    100,   # velocity
    VelocityUnits.PCT,   # velocityUnit
    True   # waitForCompletion
)
