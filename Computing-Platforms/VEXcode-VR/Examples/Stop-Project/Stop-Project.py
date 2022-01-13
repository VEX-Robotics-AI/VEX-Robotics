# -------------------------------------------------------------
# 
# 	Project:        Stop Project
#	Description:    This example will show how to stop a running
#                   project using the 'stop_project()' command
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    pen.move(DOWN)
    pen.set_pen_color(BLACK)

    # A project will run each command within the program
    for value in range(4):
        drivetrain.drive_for(FORWARD, 200, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        wait(5, MSEC)

    # The project will continue running
    # until it reaches a 'stop_project()' command
    # then the project will stop running
    stop_project()

# VR threads — Do not delete
vr_thread(main())
