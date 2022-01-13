# -------------------------------------------------------------
# 
# 	Project:        Moving Disks
#	Description:    This example will show how to Boost (pick up) 
#                   and Drop (drop) to move disks using the Electromagnet
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # Drive to the first disk
    drivetrain.drive_for(FORWARD, 750, MM)
    
    # Boost the Electromagnet to pick up the disk
    magnet.energize(BOOST)

    # Turn around and return to the goal
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 750, MM)

    # Drop the Electromagnet to drop the disk
    magnet.energize(DROP)

    # Reverse away from the disk
    drivetrain.drive_for(REVERSE, 100, MM)

# VR threads — Do not delete
vr_thread(main())
