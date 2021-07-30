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

    MOTOR_VELOCITY_PCT = 100

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

    def rest_leg_on_surface(self, leg_motor, forward=True):
        # rotate motor up to 270 degrees within 1 second
        # using max velocity but very light power/torque
        leg_motor.set_max_torque_percent(5)
        leg_motor.set_timeout(
            1,   # time,
            TimeUnits.SEC   # timeUnit
        )
        leg_motor.spin_for(
            DirectionType.FWD if forward else DirectionType.REV,   # dir
            270,   # rotation
            RotationUnits.DEG,   # rotationUnit
            100,   # velocity
            VelocityUnits.PCT,   # velocityUnit
            True   # waitForCompletion
        )

        # restore max motor power/torque to 100% again
        leg_motor.set_max_torque_percent(100)

    def reset_legs(self):
        for leg_motor in (self.front_left_motor, self.front_right_motor,
                          self.rear_left_motor, self.rear_right_motor):
            self.rest_leg_on_surface(leg_motor, True)

            # set motor encoder to 0
            leg_motor.reset_rotation()

    def rest_left_legs_forward(self):
        for leg_motor in (self.front_left_motor, self.rear_left_motor):
            self.rest_leg_on_surface(leg_motor, True)

    def rest_left_legs_backward(self):
        for leg_motor in (self.rear_left_motor, self.front_left_motor):
            self.rest_leg_on_surface(leg_motor, False)

    def rest_right_legs_forward(self):
        for leg_motor in (self.front_right_motor, self.rear_right_motor):
            self.rest_leg_on_surface(leg_motor, True)

    def rest_right_legs_backward(self):
        for leg_motor in (self.rear_right_motor, self.front_right_motor):
            self.rest_leg_on_surface(leg_motor, False)

    def remote_control_once(self):
        if self.controller.buttonEUp.pressing():
            self.rest_left_legs_forward()

        elif self.controller.buttonEDown.pressing():
            self.rest_left_legs_backward()

        elif self.controller.buttonFUp.pressing():
            self.rest_right_legs_forward()

        elif self.controller.buttonFDown.pressing():
            self.rest_right_legs_backward()

        else:
            left_velocity = self.controller.axisA.position()
            right_velocity = self.controller.axisD.position()
            self.front_left_motor.spin(
                DirectionType.FWD,   # dir
                left_velocity,   # velocity
                VelocityUnits.PCT   # velocityUnit
            )
            self.rear_left_motor.spin(
                DirectionType.FWD,   # dir
                left_velocity,   # velocity
                VelocityUnits.PCT   # velocityUnit
            )
            self.front_right_motor.spin(
                DirectionType.FWD,   # dir
                right_velocity,   # velocity
                VelocityUnits.PCT   # velocityUnit
            )
            self.rear_right_motor.spin(
                DirectionType.FWD,   # dir
                right_velocity,   # velocity
                VelocityUnits.PCT   # velocityUnit
            )

    def keep_remote_controlling(self):
        while True:
            self.remote_control_once()


ALLIE = Allie()


ALLIE.reset_legs()

ALLIE.keep_remote_controlling()
