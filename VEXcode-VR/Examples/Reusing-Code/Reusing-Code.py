# -------------------------------------------------------------
# 
# 	Project:        Reusing Code
#	Description:    This example will show how to create and use
#                   functions within your project
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Functions are created by using the 'def' keyword along with
# the name of the function, any parameters (in parenthesis) and
# finally a colon to denote the beginning of the function.
def my_function_1():
    brain.new_line()
    brain.print("Function #1 Called")

# Multiple functions can be defined within the same project 
def my_function_2():
    brain.new_line()
    brain.print("Function #2 Called")

# Add project code in "main"
def main():
    brain.clear()

    brain.print("Start of Function Calls")

    # Functions are "called" by using the name of the function like a command
    my_function_1()
    my_function_2()
    my_function_1()

    brain.new_line()
    brain.print("End of Function Calls")

# VR threads — Do not delete
vr_thread(main())
