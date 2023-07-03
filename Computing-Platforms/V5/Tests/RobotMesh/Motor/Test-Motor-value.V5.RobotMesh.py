"""robotmesh.com/studio/638a82b20e64b96eee8ea87a."""


from vex import (
    Brain, Motor,
    Ports,
    SECONDS,
    wait,
)


brain = Brain()

motor = Motor(Ports.PORT1)


motor_value = motor.value()
# assert isinstance(motor_value, int)

brain.screen.print_line(1, motor_value)


wait(3, SECONDS)
