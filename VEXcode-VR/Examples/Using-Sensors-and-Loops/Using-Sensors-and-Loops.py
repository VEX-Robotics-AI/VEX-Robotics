# -------------------------------------------------------------
#                                           
# 	Project:        Using Sensors and Loops
#	Description:    This example will use the distance sensor to
#                   determine which color line to draw based on distance
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # Begin driving forward with the pen down
    drivetrain.drive(FORWARD)
    pen.move(DOWN)

    # Check the distance sensor to draw a green line while 1 meter or further away
    while distance.get_distance(MM) > 1000: 
        pen.set_pen_color(GREEN)
        # A brief delay inside of a repeating loop to allow other resources to run
        wait(10, MSEC)

    # Check the distance sensor to draw a blue line while between 500mm and 1 meter
    while distance.get_distance(MM) > 500: 
        pen.set_pen_color(BLUE)
        # A brief delay inside of a repeating loop to allow other resources to run
        wait(10, MSEC)

    # Stop the robot once less than 500mm away from the wall
    drivetrain.stop()

# VR threads — Do not delete
vr_thread(main())
