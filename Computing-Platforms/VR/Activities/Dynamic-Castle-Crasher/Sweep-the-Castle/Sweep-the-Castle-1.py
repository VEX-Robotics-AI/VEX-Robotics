def when_started():
    # This Sweeps all the Castles blocks off of at least one of the Dynamic Castle Crasher Levels
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.drive(FORWARD)
    while not down_eye.detect(RED):
        wait(5, MSEC)
    drivetrain.drive_for(REVERSE, 200, MM)
    drivetrain.turn_to_heading(90, DEGREES)
    drivetrain.drive(FORWARD)
    while not down_eye.detect(RED):
        wait(5, MSEC)
    drivetrain.drive_for(REVERSE, 200, MM)
    drivetrain.turn_to_heading(180, DEGREES)
    drivetrain.drive(FORWARD)
    while not down_eye.detect(RED):
        wait(5, MSEC)
    drivetrain.drive_for(REVERSE, 150, MM)
    drivetrain.turn_to_heading(270, DEGREES)
    drivetrain.drive_for(REVERSE, 100, MM)
    drivetrain.drive(FORWARD)
    while not down_eye.detect(RED):
        wait(5, MSEC)
    drivetrain.drive_for(REVERSE, 175, MM)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.drive_for(REVERSE, 100, MM)
    drivetrain.drive(FORWARD)
    while not down_eye.detect(RED):
        wait(5, MSEC)
    drivetrain.drive_for(REVERSE, 200, MM)
    drivetrain.turn_to_heading(91, DEGREES)
    drivetrain.drive(FORWARD)
    while not down_eye.detect(RED):
        wait(5, MSEC)
    drivetrain.turn_to_heading(181, DEGREES)
    drivetrain.drive(FORWARD)
    while not down_eye.detect(RED):
        wait(5, MSEC)
    drivetrain.stop()

vr_thread(when_started())
