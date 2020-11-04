# -------------------------------------------------------------
# 
# 	Project:        Iterating Through a List
#	Description:    This example will show how to use iterate through
#                   a list in Python to access each member in the list
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # Create a list of values, with commas separating each value
    my_list = [2,4,6,8,10]

    # Clear the print console
    brain.clear()

    # Using a 'for loop', we can iterate through each element in the list
    for item in my_list:
        # During each iteration, the variable 'item' will be set to the value of
        # the specific element in the list.
        brain.print(item)
        brain.new_line()

    brain.print("Completed!")

# VR threads — Do not delete
vr_thread(main())
