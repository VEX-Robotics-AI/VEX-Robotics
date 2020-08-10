# This example will drive forward for one second,
# then drive in reverse for one second, then stop


from vexcode import *


def main():
    drivetrain.drive(FORWARD)
    wait(1, SECONDS)
    drivetrain.drive(REVERSE)
    wait(1, SECONDS)
    drivetrain.stop()


vr_thread(main())
