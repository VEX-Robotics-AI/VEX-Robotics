# This example creates and modifies numeric variables


from vexcode import *


def main():
    # Create a numeric variable by first coming up with a meaningful name.
    # A meaningful variable name accurately describes the value that is
    # assigned to it. Set the variable name equal to (=) a number which can
    # be an integer or decimal.
    distance_variable = 200

    # Use variables to replace numerical parameters in other commands.
    drivetrain.drive_for(FORWARD, distance_variable, MM)

    # Do calculations with your numeric variables.
    turn_variable = 15 * 6

    drivetrain.turn_for(RIGHT, turn_variable, DEGREES)

    # Or modify them inside another command before using the result as a
    # parameter.
    drivetrain.drive_for(FORWARD, distance_variable + 400, MM)

    # Use numeric variables in conditionals.
    loop_variable = 0

    pen.move(DOWN)
    pen.set_pen_color(RED)

    # This while loop will continue until the loop_variable does not equal 7
    while loop_variable != 7:
        drivetrain.drive_for(FORWARD, 200, MM)
        drivetrain.turn_for(LEFT, 50, DEGREES)

        # This will add to the loop_variable's value to reach an end to the
        # loop.
        loop_variable += 1
        wait(1, MSEC)


vr_thread(main())
