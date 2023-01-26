# -------------------------------------------------------------
# 
# 	Project:        Bumper Sensing
#	Description:    This example shows all of the available sensing 
#                   commands for the Bumper Sensor
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # Drive the robot forward
    drivetrain.drive(FORWARD)

    # A 'while true' loop will cause the following set of commands to repeat forever
    while True: 
        # Clear the screen's contents and set the cursor to top left position
        brain.clear()

        brain.print("LeftBumper Pressed: ", left_bumper.pressed())
        brain.new_line()

        brain.print("RightBumper Pressed: ", right_bumper.pressed())
        brain.new_line()

        # A brief delay to allow text to be printed without distortion or tearing
        wait(30, MSEC)

# VR threads — Do not delete
vr_thread(main())
