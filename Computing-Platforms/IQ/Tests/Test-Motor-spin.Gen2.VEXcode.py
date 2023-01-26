# drive.google.com/open?id=12uLmY55we4EHjPy3V3EV6wxGEhqYpG8I


from vex import (
    Motor,
    Ports,
    FORWARD, SECONDS,
    wait,
)


motor = Motor(Ports.PORT12)


# motor.spin(DIRECTION=FORWARD)  # compiles, DOES NOT RUN
motor.spin(direction=FORWARD)  # compiles & run

wait(1, SECONDS)
motor.stop()
wait(1, SECONDS)

# motor.spin()  # compiles, DOES NOT RUN
