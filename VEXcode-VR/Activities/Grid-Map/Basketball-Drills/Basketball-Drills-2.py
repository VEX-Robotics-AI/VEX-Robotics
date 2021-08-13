from vexcode import (
    DEGREES, FORWARD, RIGHT, MM,
    drivetrain, vr_thread
)


def when_started():
    # Drive forward and back 1 grid block
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(RIGHT, 180, DEGREES)

    # Drive forward and back 2 grid blocks
    drivetrain.drive_for(FORWARD, 400, MM)
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 400, MM)
    drivetrain.turn_for(RIGHT, 180, DEGREES)

    # Drive forward and back 4 grid blocks
    drivetrain.drive_for(FORWARD, 800, MM)
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 800, MM)


vr_thread(when_started())
