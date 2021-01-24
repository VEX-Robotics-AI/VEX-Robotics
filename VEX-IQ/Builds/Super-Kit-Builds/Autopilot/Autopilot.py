from drivetrain import Drivetrain
from vexiq import \
    ColorSensor, \
    DistanceSensor, \
    Gyro, \
    Motor, \
    TouchLed, \
    UNIT_CM


class Autopilot:
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
