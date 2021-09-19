from vex import (
    Brain, BrakeType, Controller, Motor,
    Ports, FORWARD, REVERSE, PERCENT, SECONDS
)


# CONFIGURE ROBOT PARTS
# =====================

# Brain
BRAIN = Brain()

# Base Pivot motor
BASE_PIVOT_MOTOR = Motor(Ports.PORT10)

# Shoulder motor
SHOULDER_MOTOR = Motor(Ports.PORT6,
                       True   # reverse polarity?
                       )

# Elbow motor
ELBOW_MOTOR = Motor(Ports.PORT1)

# Claw motor
CLAW_MOTOR = Motor(Ports.PORT4)
CLAW_MOTOR.set_timeout(3, SECONDS)

# Controller
CONTROLLER = Controller()
CONTROLLER.set_deadband(3)


# FUNCTIONS
# =========

# function for pivoting the Base
def pivot_base_by_controller_left_buttons():
    # pivot base right
    if CONTROLLER.buttonLDown.pressing():
        BASE_PIVOT_MOTOR.spin(REVERSE, 100, PERCENT)

    # pivot base left
    elif CONTROLLER.buttonLUp.pressing():
        BASE_PIVOT_MOTOR.spin(FORWARD, 100, PERCENT)

    else:
        BASE_PIVOT_MOTOR.stop(BrakeType.HOLD)


# function for controlling the Shoulder
def control_shoulder_by_controller_axis_d():
    controller_axis_d_position = CONTROLLER.axisD.position()

    if controller_axis_d_position:
        SHOULDER_MOTOR.spin(FORWARD, controller_axis_d_position, PERCENT)

    else:
        SHOULDER_MOTOR.stop(BrakeType.HOLD)


# function for controlling the Elbow
def control_elbow_by_controller_axis_a():
    controller_axis_a_position = CONTROLLER.axisA.position()

    if controller_axis_a_position:
        ELBOW_MOTOR.spin(FORWARD, controller_axis_a_position, PERCENT)

    else:
        ELBOW_MOTOR.stop(BrakeType.HOLD)


# function for controlling the Claw
def control_claw_by_controller_right_buttons():
    # open claw
    if CONTROLLER.buttonRDown.pressing():
        CLAW_MOTOR.spin(REVERSE, 100, PERCENT)

    # close claw
    elif CONTROLLER.buttonRUp.pressing():
        CLAW_MOTOR.spin(FORWARD, 100, PERCENT)

    else:
        CLAW_MOTOR.stop(BrakeType.HOLD)


# MAIN PROGRAM
# ============
while True:
    pivot_base_by_controller_left_buttons()
    control_shoulder_by_controller_axis_d()
    control_elbow_by_controller_axis_a()
    control_claw_by_controller_right_buttons()
