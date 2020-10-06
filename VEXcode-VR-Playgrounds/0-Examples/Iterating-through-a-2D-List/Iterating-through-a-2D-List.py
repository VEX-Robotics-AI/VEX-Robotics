# -------------------------------------------------------------
# 
# 	Project:        Iterating Through a 2D List
#	Description:    This example will show how to use iterate through a 
#                   2-dimensional list in Python to access each member in the list
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # Create a 2 dimensional list of values, with commas separating each value
    # and commas separating each row of the 2 dimensional list.
    my_list = [[2,4,6,8,10],
            [12,14,16,18,20],
            [22,24,26,28,30]]

    # Clear the print console
    brain.clear()

    # Using a 'for loop', we can iterate through each row in the list
    for row_items in my_list:
        # Using a second 'for loop', you can iterate through each element in each row
        for item in row_items:
            # During each iteration, the variable 'item' will be set to the value of
            # the specific element in the 2D list.
            brain.print(item)
            brain.print(" ")
        brain.new_line()

    brain.print("Completed!")

# VR threads — Do not delete
vr_thread(main())
