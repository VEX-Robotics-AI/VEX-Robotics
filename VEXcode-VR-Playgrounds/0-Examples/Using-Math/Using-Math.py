# -------------------------------------------------------------
# 
# 	Project:        Using Math
#	Description:    This example will show how to use math operations
#                   with variables and commands
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # Variables can store the result of a math calculation
    turnAngle = 360 / 8

    # Math operations can be used within commands directly
    drivetrain.drive_for(FORWARD, 20 * 20, MM)

    # Math operations on variables can be used within commands as well
    drivetrain.turn_for(LEFT,turnAngle + 45, DEGREES)

# VR threads — Do not delete
vr_thread(main())
