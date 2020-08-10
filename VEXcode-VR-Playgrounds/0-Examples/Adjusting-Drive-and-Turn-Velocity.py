# This example will drive the robot in a square 
# and then drive the robot in a reverse square


from vexcode import *


def main():
    # Set the turn velocity to 70%
    drivetrain.set_turn_velocity(70, PERCENT)

    # Set the drive velocity to 45%
    drivetrain.set_drive_velocity(45, PERCENT)

    # Drive in a square moving forward
    for repeat_count in range(4):
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 300, MM)
        # Brief wait needed at the end of loops for optimal performance
        wait(5, MSEC)

    # Drive in a square moving in reverse
    for repeat_count in range(4):
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.drive_for(REVERSE, 300, MM)
        # Brief wait needed at the end of loops for optimal performance
        wait(5, MSEC)


vr_thread(main())
