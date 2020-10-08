# This example uses the Location Sensor
# to find zero on the y and x axes


from vexcode import *


class VexRobot:
    def main(self):
        # The robot will drive until it passes 0 on the Y axis
        while not location.position(Y, MM) > 0:
            drivetrain.drive(FORWARD)
            # Brief wait needed at the end of every loop for optimal robot performance
            wait(5, MSEC)

        drivetrain.turn_for(RIGHT, 90, DEGREES)
        
        # The robot will drive until it passes 0 on the X axis
        while not location.position(X, MM) > 0:
            drivetrain.drive(FORWARD)
            # Brief wait needed at the end of every loop for optimal robot performance
            wait(5, MSEC)
        
        drivetrain.stop()

        stop_project()


VEX_ROBOT = VexRobot()

vr_thread(VEX_ROBOT.main())
