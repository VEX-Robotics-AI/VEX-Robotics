def when_started():
    pen.move(DOWN)
    drivetrain.turn_to_heading(90, DEGREES)
    drivetrain.drive_for(FORWARD, 500, MM)
    drivetrain.turn_to_heading(315, DEGREES)
    drivetrain.drive_for(FORWARD, 300, MM)
    drivetrain.turn_to_heading(235, DEGREES)
    drivetrain.drive_for(FORWARD, 350, MM)

vr_thread(when_started())
