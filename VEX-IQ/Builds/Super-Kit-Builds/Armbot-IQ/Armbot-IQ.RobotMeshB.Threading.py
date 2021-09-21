from sys import run_in_thread

from vex import (
    Brain,
    BrakeType,
    Bumper,
    Colorsensor,
    Controller,
    DirectionType,
    Motor,
    Ports,
    Sonar,
    TimeUnits,
    Touchled,
    VelocityUnits
)


BRAIN = Brain()

# Base Pivot motor configs
BASE_PIVOT_MOTOR = Motor(Ports.PORT10,   # index
                         False   # reverse polarity?
                         )
BASE_PIVOT_VELOCITY_PERCENT = 100

# Shoulder motor configs
SHOULDER_MOTOR = Motor(Ports.PORT6,   # index
                       True   # reverse polarity?
                       )

# Elbow motor configs
ELBOW_MOTOR = Motor(Ports.PORT1,   # index
                    False   # reverse polarity?
                    )

# Claw motor configs
CLAW_MOTOR = Motor(Ports.PORT4,   # index
                   False   # reverse polarity?
                   )
CLAW_MOTOR.set_timeout(3, TimeUnits.SEC)
CLAW_MOTOR_VELOCITY_PERCENT = 100

# sensor configs
BASE_BUMPER_SWITCH = Bumper(Ports.PORT2)
ELBOW_BUMPER_SWITCH = Bumper(Ports.PORT9)

DISTANCE_SENSOR = Sonar(Ports.PORT8)

COLOR_SENSOR = Colorsensor(Ports.PORT12,   # index
                           False,   # is_grayscale
                           700   # proximity
                           )

LEFT_TOUCH_LED = Touchled(Ports.PORT5)
RIGHT_TOUCH_LED = Touchled(Ports.PORT12)

# Controller configs
CONTROLLER = Controller()
CONTROLLER.set_deadband(3)


def pivot_base_by_controller_left_buttons():
    # pivot base right
    if CONTROLLER.buttonLDown.pressing():
        BASE_PIVOT_MOTOR.spin(
            DirectionType.REV,   # dir
            BASE_PIVOT_VELOCITY_PERCENT,   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

    # pivot base left
    elif CONTROLLER.buttonLUp.pressing():
        BASE_PIVOT_MOTOR.spin(
            DirectionType.FWD,   # dir
            BASE_PIVOT_VELOCITY_PERCENT,   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

    else:
        BASE_PIVOT_MOTOR.stop(BrakeType.HOLD)


def keep_pivoting_base_by_controller_left_buttons():
    while True:
        pivot_base_by_controller_left_buttons()


def control_shoulder_by_controller_axis_d():
    controller_axis_d_position = CONTROLLER.axisD.position()

    if ((controller_axis_d_position > 0) and
            (not BASE_BUMPER_SWITCH.pressing())) or \
            (controller_axis_d_position < 0):
        SHOULDER_MOTOR.spin(
            DirectionType.FWD,   # dir
            controller_axis_d_position,   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

    else:
        SHOULDER_MOTOR.stop(BrakeType.HOLD)


def keep_controlling_shoulder_by_controller_axis_d():
    while True:
        control_shoulder_by_controller_axis_d()


def control_elbow_by_controller_axis_a():
    controller_axis_a_position = CONTROLLER.axisA.position()

    if ((controller_axis_a_position > 0) and
            (not ELBOW_BUMPER_SWITCH.pressing())) or \
            (controller_axis_a_position < 0):
        ELBOW_MOTOR.spin(
            DirectionType.FWD,   # dir
            controller_axis_a_position,   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

    else:
        ELBOW_MOTOR.stop(BrakeType.HOLD)


def keep_controlling_elbow_by_controller_axis_a():
    while True:
        control_elbow_by_controller_axis_a()


def control_claw_by_controller_right_buttons():
    # open claw
    if CONTROLLER.buttonRDown.pressing():
        CLAW_MOTOR.spin(
            DirectionType.REV,   # dir
            CLAW_MOTOR_VELOCITY_PERCENT,   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

    # close claw
    elif CONTROLLER.buttonRUp.pressing():
        CLAW_MOTOR.spin(
            DirectionType.FWD,   # dir
            CLAW_MOTOR_VELOCITY_PERCENT,   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

    else:
        CLAW_MOTOR.stop(BrakeType.HOLD)


def keep_controlling_claw_by_controller_right_buttons():
    while True:
        control_claw_by_controller_right_buttons()


run_in_thread(keep_controlling_shoulder_by_controller_axis_d)
run_in_thread(keep_controlling_elbow_by_controller_axis_a)
run_in_thread(keep_controlling_claw_by_controller_right_buttons)
keep_pivoting_base_by_controller_left_buttons()
