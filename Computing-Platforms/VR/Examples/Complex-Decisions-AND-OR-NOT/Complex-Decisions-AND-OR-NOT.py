# -------------------------------------------------------------
# 
# 	Project:        Complex Decisions (AND OR NOT)
#	Description:    This example will use logical operators to create
#                   complex decisions based on multiple sensor inputs
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # Begin driving forward with the pen down
    drivetrain.drive(FORWARD)
    pen.move(DOWN)

    # Repeat the series of conditional statements forever
    while True:
        # The 'or' operator requires EITHER conditions to be "True" 
        # for the conditional statement to evaluate as "True"
        if distance.get_distance(MM) > 1500 or distance.get_distance(MM) < 500:
            pen.set_pen_color(BLUE)
        
        # The 'and' operator requires BOTH conditions to be "True" 
        # for the conditional statement to evaluate as "True"
        elif distance.get_distance(MM) < 1500 and distance.get_distance(MM) > 1000:
            pen.set_pen_color(GREEN)
        
        # The 'not' operator will do the inverse (opposite) of 
        # the condition's value
        elif not distance.get_distance(MM) > 1000:
            pen.set_pen_color(RED)

        # Move the robot in reverse for 100mm and stop once it reaches the wall
        if left_bumper.pressed():
            drivetrain.drive_for(REVERSE,100,MM)
        
        # A brief delay inside of a repeating loop to allow other resources to run
        wait(10,MSEC)

# VR threads — Do not delete
vr_thread(main())
