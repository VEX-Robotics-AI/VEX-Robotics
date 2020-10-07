# -------------------------------------------------------------
# 
# 	Project:        Printing Text
#	Description:    This example will show how to print text
#                   to the VR Print Console in the Monitor Tab
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # Clear the Print Console at the beginning of the project
    brain.clear()

    # Print a single line of text
    brain.print("Single line of text")

    # Move the cursor down to the next line
    brain.new_line()

    # Print two sets of text on the same line
    brain.print("Two print commands will ")
    brain.print("appear on same line")

    # Move the cursor down to the next line
    brain.new_line()

    # Set the print color (text color) to Red
    brain.set_print_color(RED)
    brain.print("This text is red!")

# VR threads — Do not delete
vr_thread(main())
