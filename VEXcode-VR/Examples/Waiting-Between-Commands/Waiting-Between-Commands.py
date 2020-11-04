# -------------------------------------------------------------
# 
# 	Project:        Waiting Between Commands
#	Description:    This example will show how to use the wait
#                   command to control the flow of your project
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # 'Non-Waiting' commands like "drive" will move the robot until told otherwise
    drivetrain.drive(FORWARD)
    wait(2, SECONDS)

    # After 2 seconds, the drivetrain is now told to stop for 3 seconds
    drivetrain.stop()
    wait(3, SECONDS)

    # 'Waiting' commands like "turn for" will stop the robot after the movement is completed
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    wait(500, MSEC)

    # Adding a wait after 'Waiting' can help observe discrete robot behaviors
    drivetrain.drive_for(FORWARD, 200, MM)
    brain.print("Drive finished!")
    brain.new_line()
    wait(2, SECONDS)
    brain.print("Wait finished!")

# VR threads — Do not delete
vr_thread(main())
