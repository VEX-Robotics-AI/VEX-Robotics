from drivetrain import Drivetrain
from vexiq import Bumper, Motor


class Clawbot:
    # drive base configs
    LEFT_MOTOR_PORT = 1
    LEFT_MOTOR_REVERSE_POLARITY = False

    RIGHT_MOTOR_PORT = 6
    RIGHT_MOTOR_REVERSE_POLARITY = True

    WHEEL_TRAVEL_MM = 200
    TRACK_MM = 176

    # sensor configs
    BUMPER_SWITCH_PORT = 8

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

        self.bumper_switch = Bumper(self.BUMPER_SWITCH_PORT)


CLAWBOT = Clawbot()


while True:
    if CLAWBOT.bumper_switch.is_pressed():
        CLAWBOT.drivetrain.turn_until(
            50,   # power
            -90   # angle_deg
        )

    else:
        CLAWBOT.drivetrain.drive(
            100,   # power
            None   # distance_mm
        )
