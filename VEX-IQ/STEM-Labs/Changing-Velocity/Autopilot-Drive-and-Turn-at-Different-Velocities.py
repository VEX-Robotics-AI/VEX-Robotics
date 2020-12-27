from drivetrain import Drivetrain
from vexiq import Motor


class Autopilot:
    LEFT_MOTOR_PORT = 1
    LEFT_MOTOR_REVERSE_POLARITY = False

    RIGHT_MOTOR_PORT = 6
    RIGHT_MOTOR_REVERSE_POLARITY = True

    WHEEL_TRAVEL_MM = 200
    TRACK_MM = 176

    def __init__(self):
        self.drivetrain = \
            Drivetrain(
                Motor(
                    self.LEFT_MOTOR_PORT,   # port
                    self.LEFT_MOTOR_REVERSE_POLARITY   # switch_polarity
                ),   # left_motor
                Motor(
                    self.RIGHT_MOTOR_PORT,   # port
                    self.RIGHT_MOTOR_REVERSE_POLARITY   # switch_polarity
                ),   # right_motor
                self.WHEEL_TRAVEL_MM,   # wheel_travel_mm
                self.TRACK_MM   # track_mm
            )


AUTOPILOT = Autopilot()


AUTOPILOT.drivetrain.drive_until(
    50,   # power
    127   # distance_mm (5 inches)
)

AUTOPILOT.drivetrain.turn_until(
    50,   # power
    -90   # angle_deg: positive to turn left, negative to turn right
)

AUTOPILOT.drivetrain.drive_until(
    25,   # power
    -127   # distance_mm (5 inches)
)

AUTOPILOT.drivetrain.turn_until(
    75,   # power
    90   # angle_deg: positive to turn left, negative to turn right
)

AUTOPILOT.drivetrain.drive_until(
    75,   # power
    127   # distance_mm (5 inches)
)

AUTOPILOT.drivetrain.turn_until(
    25,   # power
    -90   # angle_deg: positive to turn left, negative to turn right
)
