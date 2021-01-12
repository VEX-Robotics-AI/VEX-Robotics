from drivetrain import Drivetrain
from vex import \
    Brain, \
    BrakeType, \
    Bumper, \
    Colorsensor, \
    Controller, \
    DirectionType, \
    DistanceUnits, \
    Gyro, \
    Motor, \
    Ports, \
    Sonar, \
    TimeUnits, \
    Touchled, \
    VelocityUnits

from sys import run_in_thread


BRAIN = Brain()

# drive base configs
LEFT_MOTOR = \
    Motor(
        Ports.PORT1,   # index
        False   # reverse
    )
RIGHT_MOTOR = \
    Motor(
        Ports.PORT6,   # index
        True   # reverse
    )
DRIVETRAIN = \
    Drivetrain(
        LEFT_MOTOR,   # left_motor
        RIGHT_MOTOR,   # right_motor
        200,   # wheel_travel
        176,   # track_width
        DistanceUnits.MM,   # distanceUnit
        1   # gear_ratio
    )

# sensor configs
TOUCH_LED = Touchled(Ports.PORT2)
COLOR_SENSOR = \
    Colorsensor(
        Ports.PORT3,   # index
        False,   # is_grayscale
        700   # proximity
    )
GYRO_SENSOR = \
    Gyro(
        Ports.PORT4,   # index
        True   # calibrate
    )
DISTANCE_SENSOR = Sonar(Ports.PORT7)
BUMPER_SWITCH = Bumper(Ports.PORT8)

# actuator configs
ARM_MOTOR = \
    Motor(
        Ports.PORT10,   # index
        False   # reverse
    )
ARM_MOTOR_VELOCITY = 30   # %

CLAW_MOTOR = \
    Motor(
        Ports.PORT11,   # index
        False   # reverse
    )
CLAW_MOTOR.set_timeout(
    3,   # time
    TimeUnits.SEC   # timeUnit
)
CLAW_MOTOR_VELOCITY = 60   # %

# controller configs
CONTROLLER = Controller()
CONTROLLER.set_deadband(3)


def drive_once_by_controller():
    LEFT_MOTOR.spin(
        DirectionType.FWD,   # dir
        CONTROLLER.axisA.position(),   # velocity
        VelocityUnits.PCT   # velocityUnit
    )
    RIGHT_MOTOR.spin(
        DirectionType.FWD,   # dir
        CONTROLLER.axisD.position(),   # velocity
        VelocityUnits.PCT   # velocityUnit
    )


def keep_driving_by_controller():
    while True:
        drive_once_by_controller()


def lower_or_raise_arm_once_by_controller():
    if CONTROLLER.buttonLDown.pressing():
        ARM_MOTOR.spin(
            DirectionType.REV,   # dir
            ARM_MOTOR_VELOCITY,   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

    elif CONTROLLER.buttonLUp.pressing():
        ARM_MOTOR.spin(
            DirectionType.FWD,   # dir
            ARM_MOTOR_VELOCITY,   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

    else:
        ARM_MOTOR.stop(BrakeType.HOLD)


def keep_lowering_or_raising_arm_by_controller():
    while True:
        lower_or_raise_arm_once_by_controller()


def grab_or_release_object_by_controller():
    if CONTROLLER.buttonRDown.pressing():
        CLAW_MOTOR.spin(
            DirectionType.REV,   # dir
            CLAW_MOTOR_VELOCITY,   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

    elif CONTROLLER.buttonRUp.pressing():
        CLAW_MOTOR.spin(
            DirectionType.FWD,   # dir
            CLAW_MOTOR_VELOCITY,   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

    else:
        CLAW_MOTOR.stop(BrakeType.HOLD)


def keep_grabbing_or_releasing_objects_by_controller():
    while True:
        grab_or_release_object_by_controller()


if __name__ == 'TBD':
    run_in_thread(keep_lowering_or_raising_arm_by_controller)
    run_in_thread(keep_grabbing_or_releasing_objects_by_controller)
    keep_driving_by_controller()
