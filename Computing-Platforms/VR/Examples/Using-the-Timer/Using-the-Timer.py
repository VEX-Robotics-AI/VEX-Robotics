# -------------------------------------------------------------
# 
# 	Project:        Using the Timer
#	Description:    This example will use the timer to control
#                   the duration of a while loop
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # Reset the timer at the beginning of the project
    brain.timer_reset()

    # Use the timer value for a while loop's condition
    while brain.timer_time(SECONDS) < 10:
        # Clear the screen's contents and set the cursor to top left position
        brain.clear()

        brain.print("Timer: ", brain.timer_time(SECONDS))
        brain.new_line()

        # A brief delay to allow text to be printed without distortion or tearing
        wait(30, MSEC)
    
    # Once the timer reaches 10 seconds, clear the screen and let the user know
    brain.clear()
    brain.print("10 second timer is done!")

# VR threads — Do not delete
vr_thread(main())
