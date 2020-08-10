# This example creates a variable and uses it to perform actions


from vexcode import *


# Global variable must be defined outside of the main() function
my_variable = 0


def main():
    # To have a variable appear in the monitor tab,
    # it must be declared as a "global" variable and 
    # included inside the monitor_variable() command inside of quoatation marks
    global my_variable
    monitor_variable("my_variable")

    # Use the monitor tab to check the values of the robot's sensors

    # Customize which sensor values you want displayed using the monitor_sensor()
    # command. A full list of supported sensor names can be found in the help
    # document for the monitor_sensor command.
    monitor_sensor("drivetrain.is_done")

    # If you want to monitor multiple sensors, separate them using a comma
    monitor_sensor("drivetrain.is_moving",
                   "drivetrain.heading",
                   "location.position")

    # This while loop will continue until my_variable reaches 5
    # Observe how my_variable changes from 0 to 5 in the monitor tab
    # The robot will turn right 5 times
    while my_variable != 5:
        drivetrain.turn_for(RIGHT, 45, DEGREES)

        my_variable += 1

        brain.print(my_variable)
        brain.new_line()

        wait(1, SECONDS)

    wait(3, SECONDS)

    brain.clear()

    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.drive_for(FORWARD, 500, MM)
    

vr_thread(main())
