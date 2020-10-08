# -------------------------------------------------------------
# 
# 	Project:        Storing Values
#	Description:    This example will show how variables can be used
#                   to store values for later use
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # Variables can be used to set specific values to be used later in your program
    distance_to_travel = 250
    angle_to_turn = 90

    drivetrain.drive_for(FORWARD, distance_to_travel, MM)
    drivetrain.turn_for(RIGHT, angle_to_turn, DEGREES)

    # Variable values can be changed at any point in your project
    distance_to_travel = 150
    angle_to_turn = 45

    drivetrain.drive_for(FORWARD, distance_to_travel, MM)
    drivetrain.turn_for(RIGHT, angle_to_turn, DEGREES)

    # Variables values can also be used to increment a variable
    distance_to_travel = distance_to_travel + 100
    angle_to_turn = angle_to_turn + 90

    drivetrain.drive_for(FORWARD, distance_to_travel, MM)
    drivetrain.turn_for(RIGHT, angle_to_turn, DEGREES)

# VR threads — Do not delete
vr_thread(main())
