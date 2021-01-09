def when_started():
    drivetrain.drive_for(FORWARD, 300, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 300, MM)
    pen.move(DOWN)
    for repeat_count in range(4):
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 600, MM)
        wait(5, MSEC)
    drivetrain.turn_for(LEFT, 150, DEGREES)
    drivetrain.drive_for(FORWARD, 346.4, MM)
    drivetrain.turn_for(LEFT, 60, DEGREES)
    drivetrain.drive_for(FORWARD, 346.4, MM)

vr_thread(when_started())
