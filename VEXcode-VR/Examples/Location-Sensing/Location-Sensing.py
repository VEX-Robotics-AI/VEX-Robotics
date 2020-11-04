# -------------------------------------------------------------
# 
# 	Project:        Location Sensing
#	Description:    This example shows all of the available sensing 
#                   commands for the Location Sensor
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # Drive the robot forward
    drivetrain.drive(FORWARD)

    # A 'while true' loop will cause the following set of commands to repeat forever
    while True: 
        # Clear the screen's contents and set the cursor to top left position
        brain.clear()

        brain.print("Angle in degrees: ", location.position_angle(DEGREES), "degrees")
        brain.new_line()

        brain.print("X in MM: ", location.position(X, MM))
        brain.new_line()

        brain.print("Y in MM: ", location.position(Y, MM))
        brain.new_line()

        brain.print("X in Inches: ", location.position(X, INCHES))
        brain.new_line()

        brain.print("Y in Inches: ", location.position(Y, INCHES))
        brain.new_line()

        # A brief delay to allow text to be printed without distortion or tearing
        wait(30, MSEC)

# VR threads — Do not delete
vr_thread(main())
