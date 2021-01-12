from vex import Controller, DirectionType, Motor, Ports, VelocityUnits


class VRex:
    MOTOR_PORT = Ports.PORT7

    CONTROLLER_DEADBAND = 3   # seconds

    def __init__(self):
        self.motor = \
            Motor(
                self.MOTOR_PORT,   # index
                False   # reverse
            )

        self.controller = Controller()
        self.controller.set_deadband(self.CONTROLLER_DEADBAND)

    def drive_once_by_controller(self):
        self.motor.spin(
            DirectionType.FWD,   # dir
            self.controller.axisA.position(),   # velocity
            VelocityUnits.PCT   # velocityUnit
        )

    def keep_driving_by_controller(self):
        while True:
            self.drive_once_by_controller()


if __name__ == 'TBD':
    V_REX = VRex()

    V_REX.keep_driving_by_controller()
