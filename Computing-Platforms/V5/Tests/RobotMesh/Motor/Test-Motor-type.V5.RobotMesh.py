"""robotmesh.com/studio/64a33791a3776a661acced69"""


from vex import (
    Brain, Motor,
    Ports,
    SECONDS,
    wait,
)


brain = Brain()

motor = Motor(Ports.PORT1)


motor_type = motor.type()
# assert isinstance(motor_type, int)

brain.screen.print_line(1, motor_type)


wait(3, SECONDS)
