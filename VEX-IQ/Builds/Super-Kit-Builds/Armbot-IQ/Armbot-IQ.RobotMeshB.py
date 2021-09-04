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

# from sys import run_in_thread


class Armbot:
    # Base Pivot motor configs
    BASE_PIVOT_MOTOR_PORT = Ports.PORT10
    BASE_PIVOT_REVERSE_POLARITY = False
    BASE_PIVOT_VELOCITY_PERCENT = 100

    # Shoulder motor configs
    SHOULDER_MOTOR_PORT = Ports.PORT6
    SHOULDER_REVERSE_POLARITY = True   # reverse polarity

    # Elbow motor configs
    ELBOW_MOTOR_PORT = Ports.PORT1
    ELBOW_REVERSE_POLARITY = False

    # Claw motor configs
    CLAW_MOTOR_PORT = Ports.PORT4
    CLAW_MOTOR_REVERSE_POLARITY = False
    CLAW_MOTOR_VELOCITY_PERCENT = 100
    CLAW_MOTOR_TIMEOUT_SECS = 3

    # sensor configs
    BASE_BUMPER_SWITCH_PORT = Ports.PORT2
    ELBOW_BUMPER_SWITCH_PORT = Ports.PORT9
    DISTANCE_SENSOR_PORT = Ports.PORT8
    COLOR_SENSOR_PORT = Ports.PORT12
    LEFT_TOUCH_LED_PORT = Ports.PORT5
    RIGHT_TOUCH_LED_PORT = Ports.PORT11

    # controller configs
    CONTROLLER_DEADBAND = 3   # seconds

    def __init__(self):
        self.brain = Brain()

        self.base_pivot_motor = \
            Motor(
                self.BASE_PIVOT_MOTOR_PORT,   # index
                self.BASE_PIVOT_REVERSE_POLARITY   # reverse polarity?
            )

        self.shoulder_motor = \
            Motor(
                self.SHOULDER_MOTOR_PORT,   # index
                self.SHOULDER_REVERSE_POLARITY   # reverse polarity?
            )

        self.elbow_motor = \
            Motor(
                self.ELBOW_MOTOR_PORT,   # index
                self.ELBOW_REVERSE_POLARITY   # reverse polarity?
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

        self.base_bumper_switch = Bumper(self.BASE_BUMPER_SWITCH_PORT)

        self.elbow_bumper_switch = Bumper(self.ELBOW_BUMPER_SWITCH_PORT)

        self.distance_sensor = Sonar(self.DISTANCE_SENSOR_PORT)

        self.color_sensor = \
            Colorsensor(
                self.COLOR_SENSOR_PORT,   # index
                False,   # is_grayscale
                700   # proximity
            )

        self.left_touch_led = Touchled(self.LEFT_TOUCH_LED_PORT)
        self.right_touch_led = Touchled(self.RIGHT_TOUCH_LED_PORT)

        self.controller = Controller()
        self.controller.set_deadband(self.CONTROLLER_DEADBAND)

    def pivot_base_by_controller_left_buttons(self):
        # pivot base right
        if self.controller.buttonLDown.pressing():
            self.base_pivot_motor.spin(
                DirectionType.REV,   # dir
                self.BASE_PIVOT_VELOCITY_PERCENT,   # velocity
                VelocityUnits.PCT   # velocityUnit
            )

        # pivot base left
        elif self.controller.buttonLUp.pressing():
            self.base_pivot_motor.spin(
                DirectionType.FWD,   # dir
                self.BASE_PIVOT_VELOCITY_PERCENT,   # velocity
                VelocityUnits.PCT   # velocityUnit
            )

        else:
            self.base_pivot_motor.stop(BrakeType.HOLD)

    def keep_pivoting_base_by_controller_left_buttons(self):
        while True:
            self.pivot_base_by_controller_left_buttons()

    def control_shoulder_by_controller_axis_d(self):
        self.shoulder_motor.spin(
            DirectionType.FWD,   # dir
            self.controller.axisD.position(),   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

    def keep_controlling_shoulder_by_controller_axis_d(self):
        while True:
            self.lower_or_raise_arm_once_by_controller()

    def control_elbow_by_controller_axis_a(self):
        self.elbow_motor.spin(
            DirectionType.FWD,   # dir
            self.controller.axisA.position(),   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

    def keep_controlling_elbow_by_controller_axis_a(self):
        while True:
            self.control_elbow_by_controller_axis_a()

    def control_claw_by_controller_right_buttons(self):
        # open claw
        if self.controller.buttonRDown.pressing():
            self.claw_motor.spin(
                DirectionType.REV,   # dir
                self.CLAW_MOTOR_VELOCITY_PERCENT,   # velocity
                VelocityUnits.PCT   # velocityUnit
            )

        # close claw
        elif self.controller.buttonRUp.pressing():
            self.claw_motor.spin(
                DirectionType.FWD,   # dir
                self.CLAW_MOTOR_VELOCITY_PERCENT,   # velocity
                VelocityUnits.PCT   # velocityUnit
            )

        else:
            self.claw_motor.stop(BrakeType.HOLD)

    def keep_controlling_claw_by_controller_right_buttons(self):
        while True:
            self.control_claw_by_controller_right_buttons()

    def main(self):
        while True:
            self.pivot_base_by_controller_left_buttons()
            self.control_shoulder_by_controller_axis_d()
            self.control_elbow_by_controller_axis_a()
            self.control_claw_by_controller_right_buttons()


ARMBOT = Armbot()
ARMBOT.main()


# run_in_thread(ARMBOT.keep_controlling_shoulder_by_controller_axis_d)
# run_in_thread(ARMBOT.keep_controlling_elbow_by_controller_axis_a)
# run_in_thread(ARMBOT.keep_controlling_claw_by_controller_right_buttons)
# ARMBOT.keep_pivoting_base_by_controller_left_buttons()
