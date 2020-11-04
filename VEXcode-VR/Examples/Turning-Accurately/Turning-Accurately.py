# -------------------------------------------------------------
# 
# 	Project:        Turning Accurately
#	Description:    This example will show how to use different drivetrain
#                   turning commands to control the robot
#   Configuration:  VR Robot
#
# -------------------------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
def main():
    # The robot is able to turn continuously until told to stop or do something else
    drivetrain.turn(RIGHT)
    wait(4, SECONDS)
    drivetrain.stop()

    # A brief delay to observe the result of the turning action
    wait(1, SECONDS)

    # A 'Turn For' command will turn based on current orientation of the robot
    # (Current position + # of degrees)
    drivetrain.turn_for(LEFT, 180, DEGREES)

    # A brief delay to observe the result of the turning action
    wait(1, SECONDS)

    # A Drivetrain can also be used to turn to an exact heading when using a Gyro
    # based on the sensor's feedback

    # This command will point the robot back to a rotation value of 0
    # (its starting orientation) and will determine the fastest direction to turn
    drivetrain.turn_to_rotation(0, DEGREES)

# VR threads — Do not delete
vr_thread(main())
