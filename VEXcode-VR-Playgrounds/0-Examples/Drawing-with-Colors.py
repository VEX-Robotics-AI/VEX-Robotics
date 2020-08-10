# This example will draw a star using the red and blue pen


from vexcode import *


def main():
    pen.move(DOWN)
    pen.set_pen_color(RED)
    for repeat_count2 in range(5):
        for repeat_count in range(4):
            drivetrain.drive_for(FORWARD, 400, MM)
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            pen.set_pen_color(BLUE)
            # Brief wait needed at the end of loops for optimal performance
            wait(5, MSEC)
        pen.set_pen_color(RED)
        drivetrain.turn_for(RIGHT, 72, DEGREES)
        # Brief wait needed at the end of loops for optimal performance
        wait(5, MSEC)


vr_thread(main())
