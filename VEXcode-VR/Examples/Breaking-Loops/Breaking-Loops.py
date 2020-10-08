# -------------------------------------------------------------
#                                           
# 	Project:        Breaking Loops
#	Description:    This example will use a distance sensor to break
#                   a 'while true' loop in the middle of looping
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # Clear the screen and reset the print cursor to the top left corner
    brain.clear()

    # Create a variable to track the number of loop iterations
    value = 0

    # Begin driving forward
    drivetrain.drive(FORWARD)

    # A 'while true' loop will cause the following set of commands to repeat forever
    while True:
        # Increment the variable 'value' by 1 each loop
        value = value + 1

        # Print the 'value' variable showing each loop iteration
        brain.print("Loop Number #", value)
        brain.new_line()
        
        # Wait between each loop iteration
        wait(0.5, SECONDS)

        # Break (exit) the 'while true' loop early if the distance sensor detects an object within 250mm   
        if distance.get_distance(MM) < 250:
            break

    drivetrain.stop()
    brain.print("Robot Stopped - Loop Broken")

# VR threads — Do not delete
vr_thread(main())
