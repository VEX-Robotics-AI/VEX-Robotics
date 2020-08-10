# This example will use the DownEye Sensor
# to detect and pick up a disk using the Electromagnet


from vexcode import *


def main():
    # Drives forward until a blue object is detected
    while True:
        drivetrain.drive(FORWARD)

        if down_eye.detect(BLUE):
            magnet.energize(BOOST)
            drivetrain.drive_for(REVERSE, 800, MM)
            # Used to exit the while true loop and drop the disk
            break
        # Brief wait needed at the end of loops for optimal performance
        wait(5, MSEC)
        
    magnet.energize(DROP)


vr_thread(main())
