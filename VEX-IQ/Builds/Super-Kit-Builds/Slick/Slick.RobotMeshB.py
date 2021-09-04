# from sys import run_in_thread

from drivetrain import Drivetrain
from vex import (
    Brain,
    Controller,
    DirectionType,
    DistanceUnits,
    Motor,
    Ports,
    VelocityUnits
)


class Slick:
    # Drive Base configs
    LEFT_MOTOR_PORT = Ports.PORT1
    LEFT_MOTOR_REVERSE_POLARITY = False

    RIGHT_MOTOR_PORT = Ports.PORT6
    RIGHT_MOTOR_REVERSE_POLARITY = True

    WHEEL_TRAVEL = 200
    TRACK_WIDTH = 176
    DISTANCE_UNIT = DistanceUnits.MM
    GEAR_RATIO = 1

    # Controller configs
    CONTROLLER_DEADBAND = 3

    def __init__(self):
        self.brain = Brain()

        self.left_motor = \
            Motor(
                self.LEFT_MOTOR_PORT,   # index
                self.LEFT_MOTOR_REVERSE_POLARITY   # reverse polarity?
            )
        self.right_motor = \
            Motor(
                self.RIGHT_MOTOR_PORT,   # index
                self.RIGHT_MOTOR_REVERSE_POLARITY   # reverse polarity?
            )
        self.drivetrain = \
            Drivetrain(
                self.left_motor,   # left_motor
                self.right_motor,   # right_motor
                self.WHEEL_TRAVEL,   # wheel_travel
                self.TRACK_WIDTH,   # track_width
                self.DISTANCE_UNIT,   # distanceUnit
                self.GEAR_RATIO   # gear_ratio
            )

        self.controller = Controller()
        self.controller.set_deadband(self.CONTROLLER_DEADBAND)

    def drive_by_controller(self):
        self.left_motor.spin(
            DirectionType.FWD,   # dir
            self.controller.axisA.position(),   # velocity
            VelocityUnits.PCT   # velocityUnit
        )
        self.right_motor.spin(
            DirectionType.FWD,   # dir
            self.controller.axisD.position(),   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

    def keep_driving_by_controller(self):
        while True:
            self.drive_by_controller()

    def main(self):
        self.keep_driving_by_controller()


SLICK = Slick()
SLICK.main()
