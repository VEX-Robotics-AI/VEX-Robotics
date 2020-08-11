# This example will drive forward for one second,
# then drive in reverse for one second, then stop


from vexcode import *


class VexRobot:
    def main(self):
        drivetrain.drive(FORWARD)
        wait(1, SECONDS)
        drivetrain.drive(REVERSE)
        wait(1, SECONDS)
        drivetrain.stop()

        stop_project()


VEX_ROBOT = VexRobot()

vr_thread(VEX_ROBOT.main())
