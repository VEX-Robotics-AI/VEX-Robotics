# This example uses lists to store multiple values together
# It shows how to access those values within other commands


from vexcode import *


def main():
    # A list keeps track of each item by "index"
    # The index count always starts at 0

    my_list = [10, 20, 30]

    # So if you want to print the first value of my_list,
    # print the index with my_list[0]
    brain.print(my_list[0])
    brain.new_line()

    # If you want to drive forward for the value
    # of the first index in my_list
    # use the first index, or, my_list[0]
    # as the second argument in the drive_for command
    drivetrain.drive_for(FORWARD, my_list[0], INCHES)
    drivetrain.stop()

    # To use the third index value as a turn angle
    # use my_list[2] as your second argument in the turn_for command
    drivetrain.turn_for(RIGHT, my_list[2], DEGREES)

    # A 2D list also starts counting from 0 instead of 1.
    # Just like a regular list.
    my_2d_list = [
        [100, 200, 300],
        [400, 500, 600],
        [700, 800, 900]
    ]

    # Using [0] will print the entire FIRST list of my_2d_list
    brain.print(my_2d_list[0])
    brain.new_line()

    # Using [0][0] will print only the FIRST index
    # of the FIRST list of my_2d_list.
    brain.print(my_2d_list[0][0])
    brain.new_line()

    # Using [2] will print the entire THIRD list of my_2d_list
    brain.print(my_2d_list[2])
    brain.new_line()

    # Index [2] of list [2] is the THIRD number in the THIRD list
    brain.print(my_2d_list[2][2])
    drivetrain.drive_for(FORWARD, my_2d_list[2][2], MM)


vr_thread(main())
