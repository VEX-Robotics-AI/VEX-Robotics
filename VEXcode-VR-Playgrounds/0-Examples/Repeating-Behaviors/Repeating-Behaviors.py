# -------------------------------------------------------------
# 
# 	Project:        Repeating Behaviors
#	Description:    This example will show how to use a for loop
#                   to repeat a set of commands within a project
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
# Commands can run before the 'for' loop
    brain.print("Begin Driving")

    # The 'for' loop can be used to repeat actions for a set number of iterations
    # Keep in mind that actions within the `for` loop should be indented properly
    for value in range (4): 
        drivetrain.drive_for(FORWARD, 200, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)

    # After the 'for' loop has completed, any code under the 'for' loop will run
    brain.clear()
    brain.print("Completed Driving")

# VR threads — Do not delete
vr_thread(main())
