def when_started():
    drivetrain.drive_for(FORWARD, 1200, MM)
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 1200, MM)

vr_thread(when_started())
