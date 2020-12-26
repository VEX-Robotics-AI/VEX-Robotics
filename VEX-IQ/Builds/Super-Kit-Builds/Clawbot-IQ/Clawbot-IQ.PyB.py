from drivetrain import Drivetrain
from vex import \
    Brain, \
    Bumper, \
    Colorsensor, \
    Controller, \
    DirectionType, \
    DistanceUnits, \
    Gyro, \
    Motor, \
    Ports, \
    Sonar, \
    Touchled, \
    VelocityUnits


class Clawbot:
    # drive base configs
    LEFT_MOTOR_PORT = Ports.PORT1
    RIGHT_MOTOR_PORT = Ports.PORT6
    WHEEL_TRAVEL = 200
    TRACK_WIDTH = 176
    DISTANCE_UNIT = DistanceUnits.MM
    GEAR_RATIO = 1

    # sensor configs
    TOUCH_LED_PORT = Ports.PORT2
    COLOR_SENSOR_PORT = Ports.PORT3
    GYRO_SENSOR_PORT = Ports.PORT4
    DISTANCE_SENSOR_PORT = Ports.PORT7
    BUMPER_SWITCH_PORT = Ports.PORT8

    # actuator configs
    ARM_MOTOR_PORT = Ports.PORT10
    CLAW_MOTOR_PORT = Ports.PORT11

    # controller configs
    CONTROLLER_DEADBAND = 3

    def __init__(self):
        self.brain = Brain()

        self.left_motor = \
            Motor(
                self.LEFT_MOTOR_PORT,   # index
                False   # reverse
            )
        self.right_motor = \
            Motor(
                self.RIGHT_MOTOR_PORT,   # index
                True   # reverse
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

        self.arm_motor = \
            Motor(
                self.ARM_MOTOR_PORT,   # index
                False   # reverse
            )

        self.claw_motor = \
            Motor(
                self.CLAW_MOTOR_PORT,   # index
                False   # reverse
            )

        self.controller = Controller()
        self.controller.set_deadband(self.CONTROLLER_DEADBAND)

    def drive_once_by_controller(self):
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
            self.drive_once_by_controller()


CLAWBOT = Clawbot()

CLAWBOT.keep_driving_by_controller()
