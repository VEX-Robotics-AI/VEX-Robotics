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
    MOTOR_TIMEOUT_SECS = 1

    CONTROLLER_DEADBAND = 3   # seconds

    def __init__(self):
        self.front_left_motor = \
            Motor(
                self.FRONT_LEFT_MOTOR_PORT,   # index
                self.FRONT_LEFT_MOTOR_REVERSE_POLARITY   # reverse
            )
        self.front_left_motor.set_timeout(
            self.MOTOR_TIMEOUT_SECS,   # time,
            TimeUnits.SEC   # timeUnit
        )

        self.front_right_motor = \
            Motor(
                self.FRONT_RIGHT_MOTOR_PORT,   # index
                self.FRONT_RIGHT_MOTOR_REVERSE_POLARITY   # reverse
            )
        self.front_right_motor.set_timeout(
            self.MOTOR_TIMEOUT_SECS,   # time,
            TimeUnits.SEC   # timeUnit
        )

        self.rear_left_motor = \
            Motor(
                self.REAR_LEFT_MOTOR_PORT,   # index
                self.REAR_LEFT_MOTOR_REVERSE_POLARITY   # reverse
            )
        self.rear_left_motor.set_timeout(
            self.MOTOR_TIMEOUT_SECS,   # time,
            TimeUnits.SEC   # timeUnit
        )

        self.rear_right_motor = \
            Motor(
                self.REAR_RIGHT_MOTOR_PORT,   # index
                self.REAR_RIGHT_MOTOR_REVERSE_POLARITY   # reverse
            )
        self.rear_right_motor.set_timeout(
            self.MOTOR_TIMEOUT_SECS,   # time,
            TimeUnits.SEC   # timeUnit
        )

        self.controller = Controller()
        self.controller.set_deadband(self.CONTROLLER_DEADBAND)

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


if __name__ == 'TBD':
    ALLIE = Allie()

    ALLIE.keep_driving_by_controller()
