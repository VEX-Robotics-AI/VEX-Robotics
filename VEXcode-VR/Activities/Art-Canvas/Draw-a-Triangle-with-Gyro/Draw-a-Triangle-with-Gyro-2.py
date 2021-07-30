def when_started():
    pen.move(DOWN)
    drivetrain.drive_for(FORWARD, 250, MM)
    drivetrain.turn_to_heading(113, DEGREES)
    drivetrain.drive_for(FORWARD, 650, MM)
    drivetrain.turn_to_heading(270, DEGREES)
    drivetrain.drive_for(FORWARD, 600, MM)

vr_thread(when_started())
