from drivetrain import Drivetrain
from vexiq import Motor

from sys import sleep


class Clawbot:
    # drive base configs
    LEFT_MOTOR_PORT = 1
    LEFT_MOTOR_REVERSE_POLARITY = False

    RIGHT_MOTOR_PORT = 6
    RIGHT_MOTOR_REVERSE_POLARITY = True

    WHEEL_TRAVEL_MM = 200
    TRACK_MM = 176

    # actuator configs
    ARM_MOTOR_PORT = 10
    ARM_MOTOR_REVERSE_POLARITY = False

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

        self.arm_motor = \
            Motor(
                self.ARM_MOTOR_PORT,   # index
                self.ARM_MOTOR_REVERSE_POLARITY   # reverse
            )


CLAWBOT = Clawbot()


for _ in range(10):
    CLAWBOT.arm_motor.run_until(
        100,  # power
        300,   # distance
        True   # hold
    )

    CLAWBOT.drivetrain.turn_until(
        100,   # power
        -90   # angle_deg
    )

    for _ in range(9):
        CLAWBOT.drivetrain.turn_until(
            100,   # power
            10   # angle_deg
        )

        sleep(0.5)

    CLAWBOT.arm_motor.run_until(
        -100,  # power
        300,   # distance
        True   # hold
    )
