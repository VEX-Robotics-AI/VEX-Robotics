# -------------------------------------------------------------
# 
# 	Project:        Drivetrain Sensing
#	Description:    This example shows all of the available sensing 
#                   blocks for the Drivetrain
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # Begin to turn the robot and don't wait for it to finish
    drivetrain.turn_for(RIGHT, 360, DEGREES, wait=False)

    # A 'while true' loop will cause the following set of commands to repeat forever
    while True: 
        # Clear the screen's contents and set the cursor to top left position
        brain.clear()

        brain.print("drive is done?: ", drivetrain.is_done())
        brain.new_line()

        brain.print("drive is moving?: ", drivetrain.is_moving())
        brain.new_line()

        brain.print("Heading in degrees: ", drivetrain.heading(DEGREES), "degrees")
        brain.new_line()

        brain.print("Rotation in degrees: ", drivetrain.rotation(DEGREES), "degrees")
        brain.new_line()

        # A brief delay to allow text to be printed without distortion or tearing
        wait(30, MSEC)

# VR threads — Do not delete
vr_thread(main())
