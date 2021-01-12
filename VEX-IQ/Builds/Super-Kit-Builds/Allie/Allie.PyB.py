from vex import \
    Controller, \
    DirectionType, \
    Motor, \
    Ports, \
    RotationUnits, \
    TimeUnits, \
    VelocityUnits


class Allie:
    FRONT_LEFT_MOTOR_PORT = Ports.PORT1
    FRONT_LEFT_MOTOR_REVERSE_POLARITY = False

    FRONT_RIGHT_MOTOR_PORT = Ports.PORT6
    FRONT_RIGHT_MOTOR_REVERSE_POLARITY = True

    REAR_LEFT_MOTOR_PORT = Ports.PORT7
    REAR_LEFT_MOTOR_REVERSE_POLARITY = False

    REAR_RIGHT_MOTOR_PORT = Ports.PORT12
    REAR_RIGHT_MOTOR_REVERSE_POLARITY = True

    MOTOR_ROTATION_RESOLUTION_DEGS = 10

    CONTROLLER_DEADBAND = 3   # seconds

    def __init__(self):
        self.front_left_motor = \
            Motor(
                self.FRONT_LEFT_MOTOR_PORT,   # index
                self.FRONT_LEFT_MOTOR_REVERSE_POLARITY   # reverse
            )
        self.front_right_motor = \
            Motor(
                self.FRONT_RIGHT_MOTOR_PORT,   # index
                self.FRONT_RIGHT_MOTOR_REVERSE_POLARITY   # reverse
            )
        self.rear_left_motor = \
            Motor(
                self.REAR_LEFT_MOTOR_PORT,   # index
                self.REAR_LEFT_MOTOR_REVERSE_POLARITY   # reverse
            )
        self.rear_right_motor = \
            Motor(
                self.REAR_RIGHT_MOTOR_PORT,   # index
                self.REAR_RIGHT_MOTOR_REVERSE_POLARITY   # reverse
            )

        self.controller = Controller()
        self.controller.set_deadband(self.CONTROLLER_DEADBAND)

    def reset_motor(self, motor):
        # rotate motor up to 270 degrees within 1 second
        # using max velocity but very light power/torque
        motor.set_max_torque_percent(5)
        motor.set_timeout(
            1,   # time,
            TimeUnits.SEC   # timeUnit
        )
        motor.spin_for(
            DirectionType.FWD,   # dir
            270,   # rotation
            RotationUnits.DEG,   # rotationUnit
            100,   # velocity
            VelocityUnits.PCT,   # velocityUnit
            True   # waitForCompletion
        )

        # set motor encoder to 0
        motor.reset_rotation()

        # restore max motor power/torque to 100% again
        motor.set_max_torque_percent(100)

    def reset_legs(self):
        self.reset_motor(self.front_left_motor)
        self.reset_motor(self.front_right_motor)
        self.reset_motor(self.rear_left_motor)
        self.reset_motor(self.rear_right_motor)

    def drive_once_by_controller(self):
        if self.controller.buttonLDown.pressing():
            self.front_left_motor.spin_for(
                DirectionType.FWD,   # dir
                self.MOTOR_ROTATION_RESOLUTION_DEGS,   # rotation
                RotationUnits.DEG,   # rotationUnit
                100,   # velocity
                VelocityUnits.PCT,   # velocityUnit
                True   # waitForCompletion
            )

        elif self.controller.buttonLUp.pressing():
            self.front_left_motor.spin_for(
                DirectionType.REV,   # dir
                self.MOTOR_ROTATION_RESOLUTION_DEGS,   # rotation
                RotationUnits.DEG,   # rotationUnit
                100,   # velocity
                VelocityUnits.PCT,   # velocityUnit
                True   # waitForCompletion
            )

        elif self.controller.buttonRDown.pressing():
            self.front_right_motor.spin_for(
                DirectionType.FWD,   # dir
                self.MOTOR_ROTATION_RESOLUTION_DEGS,   # rotation
                RotationUnits.DEG,   # rotationUnit
                100,   # velocity
                VelocityUnits.PCT,   # velocityUnit
                True   # waitForCompletion
            )

        elif self.controller.buttonRUp.pressing():
            self.front_right_motor.spin_for(
                DirectionType.REV,   # dir
                self.MOTOR_ROTATION_RESOLUTION_DEGS,   # rotation
                RotationUnits.DEG,   # rotationUnit
                100,   # velocity
                VelocityUnits.PCT,   # velocityUnit
                True   # waitForCompletion
            )

        elif self.controller.buttonEUp.pressing():
            self.rear_left_motor.spin_for(
                DirectionType.FWD,   # dir
                self.MOTOR_ROTATION_RESOLUTION_DEGS,   # rotation
                RotationUnits.DEG,   # rotationUnit
                100,   # velocity
                VelocityUnits.PCT,   # velocityUnit
                True   # waitForCompletion
            )

        elif self.controller.buttonEDown.pressing():
            self.rear_left_motor.spin_for(
                DirectionType.REV,   # dir
                self.MOTOR_ROTATION_RESOLUTION_DEGS,   # rotation
                RotationUnits.DEG,   # rotationUnit
                100,   # velocity
                VelocityUnits.PCT,   # velocityUnit
                True   # waitForCompletion
            )

        elif self.controller.buttonFUp.pressing():
            self.rear_right_motor.spin_for(
                DirectionType.FWD,   # dir
                self.MOTOR_ROTATION_RESOLUTION_DEGS,   # rotation
                RotationUnits.DEG,   # rotationUnit
                100,   # velocity
                VelocityUnits.PCT,   # velocityUnit
                True   # waitForCompletion
            )

        elif self.controller.buttonFDown.pressing():
            self.rear_right_motor.spin_for(
                DirectionType.REV,   # dir
                self.MOTOR_ROTATION_RESOLUTION_DEGS,   # rotation
                RotationUnits.DEG,   # rotationUnit
                100,   # velocity
                VelocityUnits.PCT,   # velocityUnit
                True   # waitForCompletion
            )

    def keep_driving_by_controller(self):
        while True:
            self.drive_once_by_controller()


ALLIE = Allie()


ALLIE.reset_legs()

ALLIE.keep_driving_by_controller()
