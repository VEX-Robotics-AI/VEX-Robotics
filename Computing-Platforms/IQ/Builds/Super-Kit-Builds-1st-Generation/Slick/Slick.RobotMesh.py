# from sys import run_in_thread

from drivetrain import Drivetrain
from vexiq import Joystick, Motor


class Slick:
    # Drive Base configs
    LEFT_MOTOR_PORT = 1
    LEFT_MOTOR_REVERSE_POLARITY = False

    RIGHT_MOTOR_PORT = 6
    RIGHT_MOTOR_REVERSE_POLARITY = True

    WHEEL_TRAVEL_MM = 200
    TRACK_MM = 176

    # Controller configs
    CONTROLLER_DEADBAND = 3

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

        self.controller = Joystick()
        self.controller.set_deadband(self.CONTROLLER_DEADBAND)

    def drive_by_controller(self):
        self.left_motor.run(
            self.controller.axisA(),   # power
            None,   # distance
            False   # hold
        )
        self.right_motor.run(
            self.controller.axisD(),   # power
            None,   # distance
            False   # hold
        )

    def keep_driving_by_controller(self):
        while True:
            self.drive_by_controller()

    def main(self):
        self.keep_driving_by_controller()


SLICK = Slick()
SLICK.main()
