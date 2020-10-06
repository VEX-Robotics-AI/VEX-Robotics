# -------------------------------------------------------------
# 
# 	Project:        Drivetrain Moves and Turns
#	Description:    This example uses the drivetrain 
#                   to drive and turn in different directions
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # Driving Forward and Turning Right
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)

    # Driving Forward and Turning Left
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)

    # Driving Reverse and Turning Left
    drivetrain.drive_for(REVERSE, 200, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)

    # Driving Forward and Turning Right
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)

# VR threads — Do not delete
vr_thread(main())
