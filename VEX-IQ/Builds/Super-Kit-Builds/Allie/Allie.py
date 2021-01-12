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
    MOTOR_TIMEOUT_SECS = 1

    CONTROLLER_DEADBAND = 3   # seconds

    def __init__(self):
        self.front_left_motor = \
            Motor(
                self.FRONT_LEFT_MOTOR_PORT,   # port
                self.FRONT_LEFT_MOTOR_REVERSE_POLARITY   # switch_polarity
            )
        self.front_left_motor.stall_timeout = self.MOTOR_TIMEOUT_SECS

        self.front_right_motor = \
            Motor(
                self.FRONT_RIGHT_MOTOR_PORT,   # port
                True   # switch_polarity
            )
        self.front_right_motor.stall_timeout = self.MOTOR_TIMEOUT_SECS

        self.rear_left_motor = \
            Motor(
                self.REAR_LEFT_MOTOR_PORT,   # port
                self.REAR_LEFT_MOTOR_REVERSE_POLARITY   # switch_polarity
            )
        self.rear_left_motor.stall_timeout = self.MOTOR_TIMEOUT_SECS

        self.rear_right_motor = \
            Motor(
                self.REAR_RIGHT_MOTOR_PORT,   # port
                self.REAR_RIGHT_MOTOR_REVERSE_POLARITY   # switch_polarity
            )
        self.rear_right_motor.stall_timeout = self.MOTOR_TIMEOUT_SECS

        self.controller = Joystick()
        self.controller.set_deadband(self.CONTROLLER_DEADBAND)

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


if __name__ == 'TBD':
    ALLIE = Allie()

    ALLIE.keep_driving_by_controller()
