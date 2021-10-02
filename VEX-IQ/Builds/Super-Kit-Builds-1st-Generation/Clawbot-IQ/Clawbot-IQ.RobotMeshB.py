# from sys import run_in_thread

from drivetrain import Drivetrain
from vex import (
    Brain,
    BrakeType,
    Bumper,
    Colorsensor,
    Controller,
    DirectionType,
    DistanceUnits,
    Gyro,
    Motor,
    Ports,
    Sonar,
    TimeUnits,
    Touchled,
    VelocityUnits
)


class Clawbot:
    # Drive Base configs
    LEFT_MOTOR_PORT = Ports.PORT1
    LEFT_MOTOR_REVERSE_POLARITY = False

    RIGHT_MOTOR_PORT = Ports.PORT6
    RIGHT_MOTOR_REVERSE_POLARITY = True

    WHEEL_TRAVEL = 200
    TRACK_WIDTH = 176
    DISTANCE_UNIT = DistanceUnits.MM
    GEAR_RATIO = 1

    # Arm motor configs
    ARM_MOTOR_PORT = Ports.PORT10
    ARM_MOTOR_REVERSE_POLARITY = False
    ARM_MOTOR_VELOCITY_PERCENT = 30

    # Claw motor configs
    CLAW_MOTOR_PORT = Ports.PORT11
    CLAW_MOTOR_REVERSE_POLARITY = False
    CLAW_MOTOR_TIMEOUT_SECS = 3
    CLAW_MOTOR_VELOCITY_PERCENT = 60

    # sensor configs
    TOUCH_LED_PORT = Ports.PORT2
    COLOR_SENSOR_PORT = Ports.PORT3
    GYRO_SENSOR_PORT = Ports.PORT4
    DISTANCE_SENSOR_PORT = Ports.PORT7
    BUMPER_SWITCH_PORT = Ports.PORT8

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

        self.arm_motor = \
            Motor(
                self.ARM_MOTOR_PORT,   # index
                self.ARM_MOTOR_REVERSE_POLARITY   # reverse polarity?
            )

        self.claw_motor = \
            Motor(
                self.CLAW_MOTOR_PORT,   # index
                self.CLAW_MOTOR_REVERSE_POLARITY   # reverse polarity?
            )
        self.claw_motor.set_timeout(
            self.CLAW_MOTOR_TIMEOUT_SECS,   # time
            TimeUnits.SEC   # timeUnit
        )

        self.touch_led = Touchled(self.TOUCH_LED_PORT)

        self.color_sensor = \
            Colorsensor(
                self.COLOR_SENSOR_PORT,   # index
                False,   # is_grayscale
                700   # proximity
            )

        self.gyro_sensor = \
            Gyro(
                self.GYRO_SENSOR_PORT,   # index
                True   # calibrate
            )

        self.distance_sensor = Sonar(self.DISTANCE_SENSOR_PORT)

        self.bumper_switch = Bumper(self.BUMPER_SWITCH_PORT)

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

    def lower_or_raise_arm_by_controller(self):
        if self.controller.buttonLDown.pressing():
            self.arm_motor.spin(
                DirectionType.REV,   # dir
                self.ARM_MOTOR_VELOCITY_PERCENT,   # velocity
                VelocityUnits.PCT   # velocityUnit
            )

        elif self.controller.buttonLUp.pressing():
            self.arm_motor.spin(
                DirectionType.FWD,   # dir
                self.ARM_MOTOR_VELOCITY_PERCENT,   # velocity
                VelocityUnits.PCT   # velocityUnit
            )

        else:
            self.arm_motor.stop(BrakeType.HOLD)

    def keep_lowering_or_raising_arm_by_controller(self):
        while True:
            self.lower_or_raise_arm_by_controller()

    def grab_or_release_object_by_controller(self):
        if self.controller.buttonRDown.pressing():
            self.claw_motor.spin(
                DirectionType.REV,   # dir
                self.CLAW_MOTOR_VELOCITY_PERCENT,   # velocity
                VelocityUnits.PCT   # velocityUnit
            )

        elif self.controller.buttonRUp.pressing():
            self.claw_motor.spin(
                DirectionType.FWD,   # dir
                self.CLAW_MOTOR_VELOCITY_PERCENT,   # velocity
                VelocityUnits.PCT   # velocityUnit
            )

        else:
            self.claw_motor.stop(BrakeType.HOLD)

    def keep_grabbing_or_releasing_objects_by_controller(self):
        while True:
            self.grab_or_release_object_by_controller()

    def main(self):
        while True:
            self.drive_by_controller()
            self.lower_or_raise_arm_by_controller()
            self.grab_or_release_object_by_controller()


CLAWBOT = Clawbot()
CLAWBOT.main()


# run_in_thread(CLAWBOT.keep_lowering_or_raising_arm_by_controller)
# run_in_thread(CLAWBOT.keep_grabbing_or_releasing_objects_by_controller)
# CLAWBOT.keep_driving_by_controller()
