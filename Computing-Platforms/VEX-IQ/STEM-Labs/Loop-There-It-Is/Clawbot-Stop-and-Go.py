from drivetrain import Drivetrain
from vexiq import Motor, TouchLed, sound_note

from random import randint


class Clawbot:
    # drive base configs
    LEFT_MOTOR_PORT = 1
    LEFT_MOTOR_REVERSE_POLARITY = False

    RIGHT_MOTOR_PORT = 6
    RIGHT_MOTOR_REVERSE_POLARITY = True

    WHEEL_TRAVEL_MM = 200
    TRACK_MM = 176

    # sensor configs
    TOUCH_LED_PORT = 2

    # actuator configs
    ARM_MOTOR_PORT = 10
    ARM_MOTOR_REVERSE_POLARITY = False

    CLAW_MOTOR_PORT = 11
    CLAW_MOTOR_REVERSE_POLARITY = False

    def __init__(self):
        self.left_motor = \
            Motor(
                self.LEFT_MOTOR_PORT,   # port
                self.LEFT_MOTOR_REVERSE_POLARITY   # switch_polarity
            )
        self.right_motor = \
            Motor(
                self.RIGHT_MOTOR_PORT,   # port
                self.RIGHT_MOTOR_REVERSE_POLARITY   # switch_polarity
            )
        self.drivetrain = \
            Drivetrain(
                self.left_motor,   # left_motor
                self.right_motor,   # right_motor
                self.WHEEL_TRAVEL_MM,   # wheel_travel_mm
                self.TRACK_MM   # track_mm
            )

        self.touch_led = TouchLed(self.TOUCH_LED_PORT)

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


CLAWBOT = Clawbot()


# Have your Clawbot drive in a square.
# Before each turn:
# - The claw must be opened and closed.
# - The arm must be raised and lowered.
# - The Touch LED must show at least one color.
# - At least one sound must play.
# The Clawbot cannot drive along a side of the square more than once.
for _ in range(4):
    CLAWBOT.drivetrain.drive_until(
        100,   # power
        300   # distance_mm
    )

    CLAWBOT.claw_motor.run_until(
        -100,  # power
        90,   # distance
        True   # hold
    )
    CLAWBOT.claw_motor.run_until(
        100,  # power
        90,   # distance
        True   # hold
    )

    CLAWBOT.arm_motor.run_until(
        100,  # power
        900,   # distance
        True   # hold
    )
    CLAWBOT.arm_motor.run_until(
        -100,  # power
        900,   # distance
        True   # hold
    )

    CLAWBOT.touch_led.named_color(randint(1, 13))
    CLAWBOT.touch_led.on()

    sound_note(
        randint(1, 7),   # note
        randint(1, 7),   # octave
        0.5   # duration
    )

    CLAWBOT.drivetrain.turn_until(
        50,   # power
        -90   # angle_deg
    )
