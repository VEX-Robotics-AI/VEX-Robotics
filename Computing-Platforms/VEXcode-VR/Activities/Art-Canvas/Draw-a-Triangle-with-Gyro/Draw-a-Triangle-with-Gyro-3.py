def when_started():
    pen.move(DOWN)
    drivetrain.drive_for(FORWARD, 500, MM)
    drivetrain.turn_to_heading(120, DEGREES)
    drivetrain.drive_for(FORWARD, 1000, MM)
    drivetrain.turn_to_heading(270, DEGREES)
    drivetrain.drive_for(FORWARD, 880, MM)

vr_thread(when_started())
