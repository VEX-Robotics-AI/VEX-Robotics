from drivetrain import Drivetrain
from vexiq import Motor


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
    ARM_MOTOR_VELOCITY = 30   # %

    CLAW_MOTOR_PORT = 11
    CLAW_MOTOR_REVERSE_POLARITY = False
    CLAW_MOTOR_TIMEOUT_SECS = 3
    CLAW_MOTOR_VELOCITY = 60   # %

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

        self.claw_motor = \
            Motor(
                self.CLAW_MOTOR_PORT,   # index
                self.CLAW_MOTOR_REVERSE_POLARITY   # reverse
            )
        self.claw_motor.stall_timeout = self.CLAW_MOTOR_TIMEOUT_SECS


if __name__ == 'TBD':
    CLAWBOT = Clawbot()

    # open the Claw 75 degrees
    CLAWBOT.claw_motor.run_until(
        -100,   # power
        75,   # distance (degrees)
        True   # hold
    )

    # drive forward 150 mm to approach the object
    CLAWBOT.drivetrain.drive_until(
        100,   # power
        150,   # distance_mm
    )

    # close the Claw 60 degrees to grab the object
    CLAWBOT.claw_motor.run_until(
        100,   # power
        60,   # distance (degrees)
        True   # hold
    )

    # raise the Arm 315 degrees to lift the object
    CLAWBOT.arm_motor.run_until(
        100,   # power
        315,   # distance (degrees)
        True   # hold
    )

    # drive in reverse 150 mm to move the object to a new location
    CLAWBOT.drivetrain.drive_until(
        -100,   # power
        150,   # distance_mm
    )

    # lower the Arm 315 degrees to place the object back down
    CLAWBOT.arm_motor.run_until(
        -100,   # power
        315,   # distance (degrees)
        True   # hold
    )

    # open the Claw 60 degrees to release the object
    CLAWBOT.claw_motor.run_until(
        -100,   # power
        60,   # distance (degrees)
        True   # hold
    )
