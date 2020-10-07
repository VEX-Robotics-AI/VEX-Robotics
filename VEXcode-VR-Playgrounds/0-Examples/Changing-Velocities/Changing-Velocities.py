# -------------------------------------------------------------
# 
# 	Project:        Changing Velocities
#	Description:    This example changes the driving and
#                   turning velocity (speed) of the Drivetrain
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # Driving velocity is set from the default 50% to 100%
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.drive_for(FORWARD, 100, MM)

    # Turning velocity is set from the default 50% to 75%
    drivetrain.set_turn_velocity(75, PERCENT)
    drivetrain.turn_for(RIGHT, 90, DEGREES)

    # Driving velocity is still at 100% as drive and
    # turn speeds are set independently
    drivetrain.drive_for(FORWARD, 100, MM)

    # Turning velocity is now set at 25%
    drivetrain.set_turn_velocity(25, PERCENT)
    drivetrain.turn_for(LEFT, 90, DEGREES)

    # Driving velocity is now set at 30%
    drivetrain.set_drive_velocity(30, PERCENT)
    drivetrain.drive_for(REVERSE, 100, MM)

# VR threads — Do not delete
vr_thread(main())
