# -------------------------------------------------------------
# 
# 	Project:        Eye Sensing
#	Description:    This example shows all of the available sensing 
#                   commands for the Eye Sensor
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

        brain.print("FrontEye is near object?: ", front_eye.near_object())
        brain.new_line()

        brain.print("DownEye is near object?: ", down_eye.near_object())
        brain.new_line()

        brain.print("FrontEye brightness in %: ", front_eye.brightness(PERCENT))
        brain.new_line()

        brain.print("DownEye brightness in %: ", down_eye.brightness(PERCENT))
        brain.new_line()

        brain.print("FrontEye detects green?: ", front_eye.detect(GREEN))
        brain.new_line()

        brain.print("DownEye detects green?: ", down_eye.detect(GREEN))
        brain.new_line()

        # A brief delay to allow text to be printed without distortion or tearing
        wait(30, MSEC)

# VR threads — Do not delete
vr_thread(main())
