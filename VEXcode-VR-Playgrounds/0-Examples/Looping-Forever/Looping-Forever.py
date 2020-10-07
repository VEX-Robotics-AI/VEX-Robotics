# -------------------------------------------------------------
# 
# 	Project:        Looping Forever
#	Description:    This example will move turn the robot and will
#                   loop forever to report data on the Print Console
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # Begin turning at 20% turn velocity
    drivetrain.set_turn_velocity(20, PERCENT)
    drivetrain.turn(RIGHT)

    # A 'while true' loop will cause the following set of commands to repeat forever
    while True: 
        # Clear the screen's contents and set the cursor to top left position
        brain.clear()

        # Continuously prints the Drivetrain rotation values to the Print Console
        brain.print("Rotation: ", drivetrain.rotation(DEGREES), "degrees")

        # A brief delay to allow text to be printed without distortion or tearing
        wait(30, MSEC)

# VR threads — Do not delete
vr_thread(main())
