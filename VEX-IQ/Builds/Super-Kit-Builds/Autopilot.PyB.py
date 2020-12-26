from drivetrain import Drivetrain
from vex import \
    Brain, \
    Colorsensor, \
    DistanceUnits, \
    Gyro, \
    Motor, \
    Ports, \
    Sonar, \
    Touchled


class Autopilot:
    # drive base configs
    LEFT_MOTOR_PORT = Ports.PORT1
    LEFT_MOTOR_REVERSE_POLARITY = False

    RIGHT_MOTOR_PORT = Ports.PORT6
    RIGHT_MOTOR_REVERSE_POLARITY = True

    WHEEL_TRAVEL = 200
    TRACK_WIDTH = 176
    DISTANCE_UNIT = DistanceUnits.MM
    GEAR_RATIO = 1

    # sensor configs
    TOUCH_LED_PORT = Ports.PORT2
    COLOR_SENSOR_PORT = Ports.PORT3
    GYRO_SENSOR_PORT = Ports.PORT4
    DISTANCE_SENSOR_PORT = Ports.PORT7

    def __init__(self):
        self.brain = Brain()

        self.drivetrain = \
            Drivetrain(
                Motor(
                    self.LEFT_MOTOR_PORT,   # index
                    self.LEFT_MOTOR_REVERSE_POLARITY   # reverse
                ),   # left_motor
                Motor(
                    self.RIGHT_MOTOR_PORT,   # index
                    self.RIGHT_MOTOR_REVERSE_POLARITY   # reverse
                ),   # right_motor
                self.WHEEL_TRAVEL,   # wheel_travel
                self.TRACK_WIDTH,   # track_width
                self.DISTANCE_UNIT,   # distanceUnits
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
