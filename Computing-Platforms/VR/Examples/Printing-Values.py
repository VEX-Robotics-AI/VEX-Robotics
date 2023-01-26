# This example prints values to the Print Console
# Open the Monitor Tab to the right to see the printed values


from vexcode import *


class VexRobot:
    def main(self):
        drivetrain.drive_for(FORWARD, 600, MM)

        # Use a brain.print() to describe what is occurring in the Number Grid Map
        # Playground. View the console under the Monitor Tab.
        brain.print("The robot is at grid number thirty-one.")

        # Use a brain.new_line() to move the cursor to the next line of the console
        brain.new_line()

        wait(2, SECONDS)

        if drivetrain.is_done():
            # Print text of different colors to the console.
            # Pick a selection of colors from RED, BLACK, GREEN, and BLUE.
            brain.set_print_color(RED)
            brain.print("The robot is not moving.")
        else:
            brain.set_print_color(GREEN)    
            brain.print('The robot is moving.')

        brain.new_line()

        # After you set a print color, any prints to the console will be in that
        # color until it is changed. "The previous print color is RED" will be
        # printed in RED.
        brain.print("The set print color is RED.")

        brain.set_print_color(BLACK)

        wait(2, SECONDS)

        # Use a brain.clear() if you want to empty the printing console.
        brain.clear()

        my_number = 20

        drivetrain.turn_for(RIGHT, my_number, DEGREES)
        drivetrain.drive_for(FORWARD, 600, MM)

        # Use a brain.print() to print out sensor values.
        # Use a comma to add in an argument.
        # In this case, the heading of the robot will be printed to the console.
        brain.print("The robot is at an angle of",
                    drivetrain.heading(DEGREES),
                    "degrees.")

        brain.new_line()

        # brain.print() can print out strings.
        # Use double quotes, " ", around the strings to be printed.
        brain.print("Printing a string: The robot is at grid number sixty-two.")

        brain.new_line()

        # brain.print() can print out numbers.
        brain.print("Printing a number:", 62)

        brain.new_line()

        # brain.print() can print out variables.
        brain.print("Printing the value of my_number:", my_number)

        brain.new_line()

        # brain.print() can print out booleans.
        brain.print("Printing a boolean:", True)

        stop_project()


VEX_ROBOT = VexRobot()

vr_thread(VEX_ROBOT.main())
