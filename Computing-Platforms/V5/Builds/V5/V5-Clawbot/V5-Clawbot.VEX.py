from vex import (
    Brain, Controller, Motor,
    Ports,
    DEGREES, HOLD, FORWARD, REVERSE, PERCENT, SECONDS,
)


class Clawbot:
    # Drive Base configs
    LEFT_MOTOR_PORT = Ports.PORT1
    LEFT_MOTOR_REVERSE_POLARITY = False

    RIGHT_MOTOR_PORT = Ports.PORT10
    RIGHT_MOTOR_REVERSE_POLARITY = True

    DRIVE_VELOCITY_PERCENT = 40

    # Arm motor configs
    ARM_MOTOR_PORT = Ports.PORT8
    ARM_MOTOR_REVERSE_POLARITY = False
    ARM_MOTOR_VELOCITY_PERCENT = 30

    # Claw motor configs
    CLAW_MOTOR_PORT = Ports.PORT3
    CLAW_MOTOR_REVERSE_POLARITY = False
    CLAW_MOTOR_TIMEOUT_SECS = 3
    CLAW_MOTOR_VELOCITY_PERCENT = 50

    # Controller configs
    CONTROLLER_DEADBAND = 3

    def __init__(self):
        self.brain = Brain()

        self.left_motor = \
            Motor(
                self.LEFT_MOTOR_PORT,  # index
                self.LEFT_MOTOR_REVERSE_POLARITY  # reverse polarity?
            )
        self.right_motor = \
            Motor(
                self.RIGHT_MOTOR_PORT,  # index
                self.RIGHT_MOTOR_REVERSE_POLARITY  # reverse polarity?
            )

        self.arm_motor = \
            Motor(
                self.ARM_MOTOR_PORT,  # index
                self.ARM_MOTOR_REVERSE_POLARITY  # reverse polarity?
            )

        self.claw_motor = \
            Motor(
                self.CLAW_MOTOR_PORT,  # index
                self.CLAW_MOTOR_REVERSE_POLARITY  # reverse polarity?
            )
        self.claw_motor.set_timeout(
            self.CLAW_MOTOR_TIMEOUT_SECS,  # time
            SECONDS  # timeUnit
        )

        self.controller = Controller()
        # self.controller.set_deadband(self.CONTROLLER_DEADBAND)

    def drive_by_controller(self):
        self.left_motor.spin(
            FORWARD,  # dir
            self.controller.axis3.position()
            * self.DRIVE_VELOCITY_PERCENT / 100,  # velocity
            PERCENT  # velocityUnit
        )
        self.right_motor.spin(
            FORWARD,  # dir
            self.controller.axis2.position()
            * self.DRIVE_VELOCITY_PERCENT / 100,  # velocity
            PERCENT  # velocityUnit
        )

    def keep_driving_by_controller(self):
        while True:
            self.drive_by_controller()

    def lower_or_raise_arm_by_controller(self):
        if self.controller.buttonL2.pressing():
            self.arm_motor.spin(
                REVERSE,   # dir
                self.ARM_MOTOR_VELOCITY_PERCENT,   # velocity
                PERCENT  # velocityUnit
            )

        elif self.controller.buttonL1.pressing():
            self.arm_motor.spin(
                FORWARD,  # dir
                self.ARM_MOTOR_VELOCITY_PERCENT,  # velocity
                PERCENT  # velocityUnit
            )

        else:
            self.arm_motor.stop(HOLD)

    def keep_lowering_or_raising_arm_by_controller(self):
        while True:
            self.lower_or_raise_arm_by_controller()

    def grab_or_release_object_by_controller(self):
        if self.controller.buttonR2.pressing():
            self.claw_motor.spin(
                REVERSE,  # dir
                self.CLAW_MOTOR_VELOCITY_PERCENT,  # velocity
                PERCENT  # velocityUnit
            )

        elif self.controller.buttonR1.pressing():
            self.claw_motor.spin(
                FORWARD,  # dir
                self.CLAW_MOTOR_VELOCITY_PERCENT,  # velocity
                PERCENT  # velocityUnit
            )

        else:
            self.claw_motor.stop(HOLD)

    def keep_grabbing_or_releasing_objects_by_controller(self):
        while True:
            self.grab_or_release_object_by_controller()

    def main(self):
        self.arm_motor.spin_for(FORWARD, 180, DEGREES)

        while True:
            self.drive_by_controller()
            self.lower_or_raise_arm_by_controller()
            self.grab_or_release_object_by_controller()


CLAWBOT = Clawbot()
CLAWBOT.main()
