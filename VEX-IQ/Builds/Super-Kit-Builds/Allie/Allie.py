from vexiq import Joystick, Motor


class Allie:
    FRONT_LEFT_MOTOR_PORT = 1
    FRONT_LEFT_MOTOR_REVERSE_POLARITY = False

    FRONT_RIGHT_MOTOR_PORT = 6
    FRONT_RIGHT_MOTOR_REVERSE_POLARITY = True

    REAR_LEFT_MOTOR_PORT = 7
    REAR_LEFT_MOTOR_REVERSE_POLARITY = False

    REAR_RIGHT_MOTOR_PORT = 12
    REAR_RIGHT_MOTOR_REVERSE_POLARITY = True

    MOTOR_ROTATION_RESOLUTION_DEGS = 10

    CONTROLLER_DEADBAND = 3   # seconds

    def __init__(self):
        self.front_left_motor = \
            Motor(
                self.FRONT_LEFT_MOTOR_PORT,   # port
                self.FRONT_LEFT_MOTOR_REVERSE_POLARITY   # switch_polarity
            )
        self.front_right_motor = \
            Motor(
                self.FRONT_RIGHT_MOTOR_PORT,   # port
                True   # switch_polarity
            )
        self.rear_left_motor = \
            Motor(
                self.REAR_LEFT_MOTOR_PORT,   # port
                self.REAR_LEFT_MOTOR_REVERSE_POLARITY   # switch_polarity
            )
        self.rear_right_motor = \
            Motor(
                self.REAR_RIGHT_MOTOR_PORT,   # port
                self.REAR_RIGHT_MOTOR_REVERSE_POLARITY   # switch_polarity
            )

        self.controller = Joystick()
        self.controller.set_deadband(self.CONTROLLER_DEADBAND)

    def reset_motor(self, motor):
        # rotate motor up to 270 degrees within 1 second
        # using max velocity but very light power/torque
        # ...

        # set motor encoder to 0
        motor.reset_position()

        # restore max motor power/torque to 100% again
        # ...

    def reset_legs(self):
        self.reset_motor(self.front_left_motor)
        self.reset_motor(self.front_right_motor)
        self.reset_motor(self.rear_left_motor)
        self.reset_motor(self.rear_right_motor)

    def drive_once_by_controller(self):
        if self.controller.bLdown():
            self.front_left_motor.run_until(
                100,   # power
                self.MOTOR_ROTATION_RESOLUTION_DEGS,   # distance
                True   # hold
            )

        elif self.controller.bLup():
            self.front_left_motor.run_until(
                -100,   # power
                self.MOTOR_ROTATION_RESOLUTION_DEGS,   # distance
                True   # hold
            )

        elif self.controller.bRdown():
            self.front_right_motor.run_until(
                100,   # power
                self.MOTOR_ROTATION_RESOLUTION_DEGS,   # distance
                True   # hold
            )

        elif self.controller.bRup():
            self.front_right_motor.run_until(
                -100,   # power
                self.MOTOR_ROTATION_RESOLUTION_DEGS,   # distance
                True   # hold
            )

        elif self.controller.bEup():
            self.rear_left_motor.run_until(
                100,   # power
                self.MOTOR_ROTATION_RESOLUTION_DEGS,   # distance
                True   # hold
            )

        elif self.controller.bEdown():
            self.rear_left_motor.run_until(
                -100,   # power
                self.MOTOR_ROTATION_RESOLUTION_DEGS,   # distance
                True   # hold
            )

        elif self.controller.bFup():
            self.rear_right_motor.run_until(
                100,   # power
                self.MOTOR_ROTATION_RESOLUTION_DEGS,   # distance
                True   # hold
            )

        elif self.controller.bFdown():
            self.rear_right_motor.run_until(
                -100,   # power
                self.MOTOR_ROTATION_RESOLUTION_DEGS,   # distance
                True   # hold
            )

    def keep_driving_by_controller(self):
        while True:
            self.drive_once_by_controller()


ALLIE = Allie()


# NOTE:
# we must manually put Allie's legs down, touching the surface first
# before running the program
ALLIE.reset_legs()

ALLIE.keep_driving_by_controller()
