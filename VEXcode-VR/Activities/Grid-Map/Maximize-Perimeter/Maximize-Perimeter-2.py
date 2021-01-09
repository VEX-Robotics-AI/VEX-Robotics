def when_started():
    drivetrain.drive_for(FORWARD, 100, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    # moved 500mm to move away from the wall
    drivetrain.drive_for(FORWARD, 500, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    pen.move(DOWN)
    pen.set_pen_color(BLUE)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    # each line is 200mm, and we make 8 in the shape of an octogon
    for repeat_count in range(8):
        drivetrain.drive_for(FORWARD, 200, MM)
        drivetrain.turn_for(LEFT, 45, DEGREES)
        wait(5, MSEC)

vr_thread(when_started())
