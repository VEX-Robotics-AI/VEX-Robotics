# ------------------------------------------
#                                           
# 	Project:        Printing Values
#	Description:    This example will print the timer's value 
#                   to the VR Print Console in the Monitor Tab
#   Configuration:  VR Robot            
#                                           
# ------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # A 'while true' loop will cause the following set of commands to repeat forever
    while True:
        # Each iteration of the loop will clear the Print Console
        brain.clear()

        # Print a label and the value of the timer (to 1 decimal place)
        # as two separate print commands
        brain.print("Timer (SEC): ")
        brain.print(brain.timer_time(SECONDS), precision=1)

        # Move the cursor to the next line
        brain.new_line()

        # Print the label and value of the timer as a single command (to 3 decimal places)
        brain.print("Timer (SEC):", brain.timer_time(SECONDS), precision=3)
        
        # A brief delay to allow text to be printed without distortion or tearing
        wait(.03,SECONDS)

# VR threads — Do not delete
vr_thread(main())
