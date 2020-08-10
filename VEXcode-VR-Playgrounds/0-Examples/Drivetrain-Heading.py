# This example will turn for a random number of degrees between 10 and 300 
# It will draw in red if the Drivetrain heading is greater than 180 degrees
# It will draw in green if the Drivetrain heading is less than 180 degrees


from vexcode import *


def main():
    pen.move(DOWN)

    while True:
        drivetrain.turn_for(RIGHT, random.randint((10), 300), DEGREES)

        # If the Drivetrain heading is greater than 180 degrees it will draw in red
        # Otherwise it will draw in green
        if drivetrain.heading(DEGREES) > 180:
            pen.set_pen_color(RED)
        else:
            pen.set_pen_color(GREEN)
        drivetrain.drive_for(FORWARD, 200, MM)

        # Brief wait needed at the end of every loop for optimal robot performance
        wait(5, MSEC)


vr_thread(main())
