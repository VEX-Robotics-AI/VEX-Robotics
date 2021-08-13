from vexcode import (
    FORWARD, REVERSE, MM,
    drivetrain, vr_thread
)


def when_started():
    # Drive forward and back 1 grid block
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.drive_for(REVERSE, 200, MM)

    # Drive forward and back 2 grid blocks
    drivetrain.drive_for(FORWARD, 400, MM)
    drivetrain.drive_for(REVERSE, 400, MM)

    # Drive forward and back 4 grid blocks
    drivetrain.drive_for(FORWARD, 800, MM)
    drivetrain.drive_for(REVERSE, 800, MM)


vr_thread(when_started())
