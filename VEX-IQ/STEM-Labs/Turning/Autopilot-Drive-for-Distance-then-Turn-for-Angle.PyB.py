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
    def __init__(
            self,
            left_motor_port=Ports.PORT1, right_motor_port=Ports.PORT6,
            wheel_travel=200, track_width=176,
            distance_unit=DistanceUnits.MM,
            gear_ratio=1):
        self.drivetrain = \
            Drivetrain(
                Motor(
                    left_motor_port,   # index
                    False   # reverse
                ),   # left_motor
                Motor(
                    right_motor_port,   # index
                    True   # reverse
                ),   # right_motor
                wheel_travel,   # wheel_travel
                track_width,   # track_width
                distance_unit,   # distanceUnits
                gear_ratio   # gear_ratio
            )


AUTOPILOT = Autopilot()

AUTOPILOT.drivetrain.drive_for(
    DirectionType.FWD,   # directionType
    12,   # distance
    DistanceUnits.IN,   # distanceUnits
    100,   # velocity
    VelocityUnits.PCT,   # velocityUnits
    True   # waitForCompletion
)

AUTOPILOT.drivetrain.turn_for(
    TurnType.LEFT,   # turnType
    90,   # angle
    RotationUnits.DEG,   # rotationUnits
    100,   # velocity
    VelocityUnits.PCT,   # velocityUnits
    True   # waitForCompletion
)
