from vexiq import Joystick, Motor


class VRex:
    MOTOR_PORT = 7

    CONTROLLER_DEADBAND = 3   # seconds

    def __init__(self):
        self.motor = \
            Motor(
                self.MOTOR_PORT,   # port
                False   # switch_polarity
            )

        self.controller = Joystick()
        self.controller.set_deadband(self.CONTROLLER_DEADBAND)

    def drive_once_by_controller(self):
        self.motor.run(
            self.controller.axisA(),   # power
            None,   # distance
            False   # hold
        )

    def keep_driving_by_controller(self):
        while True:
            self.drive_once_by_controller()


if __name__ == 'TBD':
    V_REX = VRex()

    V_REX.keep_driving_by_controller()
