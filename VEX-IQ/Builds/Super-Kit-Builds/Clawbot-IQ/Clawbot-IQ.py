from drivetrain import Drivetrain
from vexiq import \
    Bumper, \
    ColorSensor, \
    DistanceSensor, \
    Gyro, \
    Joystick, \
    Motor, \
    TouchLed, \
    UNIT_CM

from sys import run_in_thread


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
    COLOR_SENSOR_PORT = 3
    GYRO_SENSOR_PORT = 4
    DISTANCE_SENSOR_PORT = 7
    DISTANCE_SENSOR_UNIT = UNIT_CM
    BUMPER_SWITCH_PORT = 8

    # actuator configs
    ARM_MOTOR_PORT = 10
    ARM_MOTOR_REVERSE_POLARITY = False
    ARM_MOTOR_VELOCITY = 30   # %

    CLAW_MOTOR_PORT = 11
    CLAW_MOTOR_REVERSE_POLARITY = False
    CLAW_MOTOR_TIMEOUT_SECS = 3
    CLAW_MOTOR_VELOCITY = 60   # %

    # controller configs
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

        self.touch_led = TouchLed(self.TOUCH_LED_PORT)

        self.color_sensor = \
            ColorSensor(
                self.COLOR_SENSOR_PORT,   # index
                False,   # is_grayscale
                700   # proximity
            )

        self.gyro_sensor = \
            Gyro(
                self.GYRO_SENSOR_PORT,   # index
                True   # calibrate
            )

        self.distance_sensor = \
            DistanceSensor(
                self.DISTANCE_SENSOR_PORT,   # port
                self.DISTANCE_SENSOR_UNIT   # unit
            )

        self.bumper_switch = Bumper(self.BUMPER_SWITCH_PORT)

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

        self.controller = Joystick()
        self.controller.set_deadband(self.CONTROLLER_DEADBAND)

    def drive_once_by_controller(self):
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
            self.drive_once_by_controller()

    def lower_or_raise_arm_once_by_controller(self):
        if self.controller.bLdown():
            self.arm_motor.run(
                -self.ARM_MOTOR_VELOCITY,   # power
                None,   # distance
                False   # hold
            )

        elif self.controller.bLup():
            self.arm_motor.run(
                self.ARM_MOTOR_VELOCITY,   # power
                None,   # distance
                False   # hold
            )

        else:
            self.arm_motor.hold()

    def keep_lowering_or_raising_arm_by_controller(self):
        while True:
            self.lower_or_raise_arm_once_by_controller()

    def grab_or_release_object_by_controller(self):
        if self.controller.bRdown():
            self.claw_motor.run(
                -self.CLAW_MOTOR_VELOCITY,   # power
                None,   # distance
                False   # hold
            )

        elif self.controller.bRup():
            self.claw_motor.run(
                self.CLAW_MOTOR_VELOCITY,   # power
                None,   # distance
                False   # hold
            )

        else:
            self.claw_motor.hold()

    def keep_grabbing_or_releasing_objects_by_controller(self):
        while True:
            self.grab_or_release_object_by_controller()


CLAWBOT = Clawbot()


while True:
    CLAWBOT.drive_once_by_controller()
    CLAWBOT.lower_or_raise_arm_once_by_controller()
    CLAWBOT.grab_or_release_object_by_controller()


# run_in_thread(CLAWBOT.keep_lowering_or_raising_arm_by_controller)
# run_in_thread(CLAWBOT.keep_grabbing_or_releasing_objects_by_controller)
# CLAWBOT.keep_driving_by_controller()
