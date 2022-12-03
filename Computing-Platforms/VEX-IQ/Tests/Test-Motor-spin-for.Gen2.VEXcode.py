# drive.google.com/open?id=12v36_xyEdSuUzU760v6wBcyaeZpxgLcC


from vex import (
    Motor,
    Ports,
    FORWARD, DEGREES,
)


motor = Motor(Ports.PORT12)


# motor.spin_for(DIRECTION=FORWARD, AMOUNT=360, UNITS=DEGREES)
#   compiles, DOES NOT RUN
# motor.spin_for(direction=FORWARD, angle=360, units=DEGREES, wait=True)
#   compiles, DOES NOT RUN
# motor.spin_for(FORWARD, angle=360, units=DEGREES, wait=True)
#   compiles, DOES NOT RUN
# motor.spin_for(FORWARD, amount=360, units=DEGREES, wait=True)
#   compiles, DOES NOT RUN
motor.spin_for(FORWARD, 360, units=DEGREES, wait=True)  # compiles & run
motor.spin_for(FORWARD, 360, DEGREES, wait=True)  # compiles & run
motor.spin_for(FORWARD, 360, DEGREES, True)  # compiles & run
motor.spin_for(FORWARD, 360, DEGREES)  # compiles & run
motor.spin_for(FORWARD, 360)  # compiles & run
# motor.spin_for(FORWARD)  # compiles, DOES NOT RUN
# motor.spin_for()  # compiles, DOES NOT RUN
