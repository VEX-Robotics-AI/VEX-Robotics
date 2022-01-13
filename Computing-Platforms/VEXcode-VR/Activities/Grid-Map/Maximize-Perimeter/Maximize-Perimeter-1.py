def when_started():
    drivetrain.drive_for(FORWARD, 100, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 100, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    pen.move(DOWN)
    pen.set_pen_color(BLUE)
    # moved 1600 mm
    for repeat_count in range(8):
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    # moved 1600 mm
    for repeat_count2 in range(8):
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    # moved 1600 mm
    for repeat_count3 in range(8):
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    # moved 1600 mm
    for repeat_count4 in range(8):
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    # perimeter: 6400 mm

vr_thread(when_started())
