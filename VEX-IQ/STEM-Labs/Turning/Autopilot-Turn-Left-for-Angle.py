from drivetrain import Drivetrain
from vexiq import Motor


class Autopilot:
    def __init__(
            self,
            left_motor_port=1, right_motor_port=6,
            wheel_travel_mm=200, track_mm=176):
        self.drivetrain = \
            Drivetrain(
                Motor(
                    left_motor_port,   # port
                    False   # switch_polarity
                ),   # left_motor
                Motor(
                    right_motor_port,   # port
                    True   # switch_polarity
                ),   # right_motor
                wheel_travel_mm,   # wheel_travel_mm
                track_mm   # track_mm
            )


AUTOPILOT = Autopilot()

AUTOPILOT.drivetrain.turn_until(
    100,   # power
    90   # angle_deg: positive to turn left, negative to turn right
)
