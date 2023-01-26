# This example uses for loops to change the Pen color


from vexcode import *


class VexRobot:
    def main(self):
        my_list = [RED, BLUE, GREEN]
        pen.move(DOWN)

        # Use a for loop to change the color of the pen.
        for value in my_list: 
            pen.set_pen_color(value)
            drivetrain.drive_for(FORWARD, 200, MM)
            wait(5, MSEC)

        stop_project()


VEX_ROBOT = VexRobot()

vr_thread(VEX_ROBOT.main())
