# -------------------------------------------------------------
# 
# 	Project:        Passing Parameters
#	Description:    This example will show how to create and use
#                   functions with parameters within your project
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Functions are created by using the 'def' keyword along with
# the name of the function, any parameters will be defined in the parenthesis
# finally a colon to denote the beginning of the function.
def my_function_1(parameter1):
    brain.new_line()
    brain.print("Function #1 Values:", parameter1)

# Multiple functions can be defined within the same project
# Multiple parameters are separated by a comma
def my_function_2(parameter1, parameter2):
    brain.new_line()
    brain.print("Function #2 Values: ")
    brain.print(parameter1)
    brain.print(", ")
    brain.print(parameter2)

# Add project code in "main"
def main():
    brain.clear()

    brain.print("Start of Function Calls")

    # Functions are "called" by using the name of the function like a command
    # and passing the values of each parameters within the parenthesis
    my_function_1(50)
    my_function_2(100, 200)
    my_function_1(300)

    brain.new_line()
    brain.print("End of Function Calls")

# VR threads — Do not delete
vr_thread(main())
