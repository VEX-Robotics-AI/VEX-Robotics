# -------------------------------------------------------------
# 
# 	Project:        Making Decisions
#	Description:    This example will use the right Bumper sensor to
#                   detect when the robot has driven into a wall or object
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # A 'while true' loop will cause the following set of commands to repeat forever
    while True:
        # A conditional statement to stop driving if the Bumper is pressed
        if right_bumper.pressed(): 
            drivetrain.stop()
        # And the else condition will drive forward if the Bumper is not pressed
        else:
            drivetrain.drive(FORWARD)
    
        # A brief delay inside of a repeating loop to allow other resources to run
        wait(10,MSEC)

# VR threads — Do not delete
vr_thread(main())
