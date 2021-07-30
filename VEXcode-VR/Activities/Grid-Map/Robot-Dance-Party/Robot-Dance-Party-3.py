def when_started():
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    for repeat_count in range(5):
        drivetrain.drive_for(FORWARD, 200, MM)
        drivetrain.turn_for(RIGHT, 20, DEGREES)
        wait(5, MSEC)
    for repeat_count4 in range(5):
        for repeat_count2 in range(10):
            drivetrain.turn_for(RIGHT, 5, DEGREES)
            drivetrain.drive_for(REVERSE, 10, MM)
            wait(5, MSEC)
        for repeat_count3 in range(10):
            drivetrain.turn_for(RIGHT, 10, DEGREES)
            pen.set_pen_color(RED)
            drivetrain.turn_for(LEFT, 10, DEGREES)
            pen.set_pen_color(BLUE)
            wait(5, MSEC)
        pen.set_pen_color(GREEN)
        drivetrain.turn_for(RIGHT, 45, DEGREES)
        drivetrain.drive_for(FORWARD, 100, MM)
        drivetrain.turn_for(RIGHT, 180, DEGREES)
        drivetrain.drive_for(REVERSE, 100, MM)
        wait(5, MSEC)
    drivetrain.turn_for(RIGHT, 360, DEGREES)

vr_thread(when_started())
