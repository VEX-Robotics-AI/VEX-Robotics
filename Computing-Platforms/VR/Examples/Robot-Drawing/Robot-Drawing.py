# ------------------------------------------
#                                           
# 	Project:        Robot Drawing
#	Description:    This example will draw lines on the playground
#                   and show how to change the colors of lines
#   Configuration:  VR Robot            
#                                           
# ------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # The pen set to "DOWN" will draw lines while the robot is moving
    pen.move(DOWN)
    drivetrain.drive_for(FORWARD, 200, MM)
    
    # The pen can also change colors from BLACK to GREEN, RED, or BLUE
    pen.set_pen_color(GREEN)
    drivetrain.drive_for(FORWARD, 200, MM)

    # Set the pen to "UP" to stop drawing lines while moving
    pen.move(UP)
    drivetrain.drive_for(FORWARD, 200, MM)

    # Control the color and movement of the pen to control where 
    # to draw lines on the Playground surface
    pen.move(DOWN)
    pen.set_pen_color(RED)
    drivetrain.drive_for(FORWARD, 200, MM)    

# VR threads — Do not delete
vr_thread(main())
