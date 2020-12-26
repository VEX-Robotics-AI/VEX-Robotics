from drivetrain import Drivetrain
from vex import \
    Brain, \
    BrakeType, \
    Bumper, \
    Colorsensor, \
    DirectionType, \
    DistanceUnits, \
    Gyro, \
    Motor, \
    Ports, \
    Sonar, \
    Touchled, \
    VelocityUnits


class Clawbot:
    def __init__(
            self,
            left_motor_port=Ports.PORT1, right_motor_port=Ports.PORT6,
            wheel_travel=200, track_width=176,
            distance_unit=DistanceUnits.MM,
            gear_ratio=1,
            touch_led_port=Ports.PORT2,
            color_sensor_port=Ports.PORT3,
            gyro_sensor_port=Ports.PORT4,
            distance_sensor_port=Ports.PORT7,
            bumper_switch_port=Ports.PORT8,
            arm_motor_port=Ports.PORT10,
            claw_motor_port=Ports.PORT11):
        self.brain = Brain()

        self.drivetrain = \
            Drivetrain(
                Motor(
                    left_motor_port,   # index
                    False   # reverse
                ),   # left_motor
                Motor(
                    right_motor_port,   # index
                    True   # reverse
                ),   # right_motor
                wheel_travel,   # wheel_travel
                track_width,   # track_width
                distance_unit,   # distanceUnits
                gear_ratio   # gear_ratio
            )

        self.touch_led = Touchled(touch_led_port)

        self.color_sensor = \
            Colorsensor(
                color_sensor_port,   # index
                False,   # is_grayscale
                700   # proximity
            )

        self.gyro_sensor = \
            Gyro(
                gyro_sensor_port,   # index
                True   # calibrate
            )

        self.distance_sensor = Sonar(distance_sensor_port)

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
    if CLAWBOT.brain.buttonUp.pressing():
        CLAWBOT.drivetrain.drive(
            DirectionType.FWD,   # directionType
            100,   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

        while CLAWBOT.brain.buttonUp.pressing():
            pass

    elif CLAWBOT.brain.buttonDown.pressing():
        CLAWBOT.drivetrain.drive(
            DirectionType.REV,   # directionType
            100,   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

        while CLAWBOT.brain.buttonDown.pressing():
            pass

    else:
        CLAWBOT.drivetrain.stop(BrakeType.COAST)
