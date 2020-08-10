# This example uses for loops to change the Pen color


from vexcode import *


def main():
    my_list = [RED, BLUE, GREEN]
    pen.move(DOWN)

    # Use a for loop to change the color of the pen.
    for value in my_list: 
        pen.set_pen_color(value)
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)


vr_thread(main())
