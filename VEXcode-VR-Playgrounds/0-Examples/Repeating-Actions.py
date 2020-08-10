# The robot will move in a 200mm by 200mm square.
# repeat_count is an iterating variable that goes up to 4
# that increments with each iteration of the for loop.


from vexcode import *


def main():
    for repeat_count in range(4):
        drivetrain.drive_for(FORWARD, 200, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        
        # Brief wait needed at the end of loops for optimal performance
        wait(5, MSEC)


vr_thread(main())
