from drivetrain import Drivetrain
from vexiq import \
    Bumper, \
    ColorSensor, \
    DistanceSensor, \
    Gyro, \
    Motor, \
    TouchLed, \
    UNIT_CM, \
    is_up_button_pressed, is_down_button_pressed


class Clawbot:
    def __init__(
            self,
            left_motor_port=1, right_motor_port=6,
            wheel_travel_mm=200, track_mm=176,
            touch_led_port=2,
            color_sensor_port=3,
            gyro_sensor_port=4,
            distance_sensor_port=7,
            bumper_switch_port=8,
            arm_motor_port=10,
            claw_motor_port=11):
        self.drivetrain = \
            Drivetrain(
                Motor(
                    left_motor_port,   # port
                    False   # switch_polarity
                ),   # left_motor
                Motor(
                    right_motor_port,   # port
                    True   # switch_polarity
                ),   # right_motor
                wheel_travel_mm,   # wheel_travel_mm
                track_mm   # track_mm
            )

        self.touch_led = TouchLed(touch_led_port)

        self.color_sensor = \
            ColorSensor(
                color_sensor_port,   # index
                False,   # is_grayscale
                700   # proximity
            )

        self.gyro_sensor = \
            Gyro(
                gyro_sensor_port,   # index
                True   # calibrate
            )

        self.distance_sensor = \
            DistanceSensor(
                distance_sensor_port,   # port
                UNIT_CM   # unit
            )

        self.bumper_switch = Bumper(bumper_switch_port)

        self.arm_motor = \
            Motor(
                arm_motor_port,   # index
                False   # reverse
            )

        self.claw_motor_port = \
            Motor(
                claw_motor_port,   # index
                False   # reverse
            )


CLAWBOT = Clawbot()

while True:
    if is_up_button_pressed():
        CLAWBOT.arm_motor.run(
            100,   # power,
            None,   # distance
            False   # hold
        )

    elif is_down_button_pressed():
        CLAWBOT.arm_motor.run(
            -100,   # power,
            None,   # distance
            False   # hold
        )

    else:
        CLAWBOT.arm_motor.hold()
