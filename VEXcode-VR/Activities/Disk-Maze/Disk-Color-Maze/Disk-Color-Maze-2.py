def when_started():
    drivetrain.drive_for(FORWARD, 200, MM)
    while not down_eye.detect(RED):
        if down_eye.detect(GREEN):
            drivetrain.turn_for(RIGHT, 90, DEGREES)
        else:
            drivetrain.drive(FORWARD)
        if down_eye.detect(BLUE):
            drivetrain.turn_for(LEFT, 90, DEGREES)
        else:
            drivetrain.drive(FORWARD)
        wait(5, MSEC)
    drivetrain.stop()

vr_thread(when_started())
