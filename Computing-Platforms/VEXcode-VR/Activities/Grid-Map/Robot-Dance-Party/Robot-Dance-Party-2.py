def when_started():
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    # move to the center
    for repeat_count in range(10):
        drivetrain.drive_for(FORWARD, 100, MM)
        drivetrain.turn_for(RIGHT, 10, DEGREES)
        wait(5, MSEC)
    drivetrain.turn_to_rotation(180, DEGREES)
    # spin 3 times
    for repeat_count2 in range(3):
        drivetrain.turn_for(RIGHT, 360, DEGREES)
        wait(5, MSEC)
    # step to the right
    drivetrain.turn_to_heading(90, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.drive_for(REVERSE, 200, MM)
    # step to the left
    drivetrain.turn_to_heading(270, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.drive_for(REVERSE, 200, MM)
    # freestyle!
    for repeat_count4 in range(2):
        for repeat_count3 in range(5):
            drivetrain.drive_for(REVERSE, 40, MM)
            drivetrain.turn_for(RIGHT, 10, DEGREES)
            drivetrain.drive_for(FORWARD, 40, MM)
            drivetrain.turn_for(LEFT, 10, DEGREES)
            wait(5, MSEC)
        drivetrain.turn_for(RIGHT, 180, DEGREES)
        wait(5, MSEC)
    # go back home again
    for repeat_count5 in range(10):
        drivetrain.drive_for(FORWARD, 100, MM)
        drivetrain.turn_for(LEFT, 10, DEGREES)
        wait(5, MSEC)
    drivetrain.turn_to_heading(0, DEGREES)

vr_thread(when_started())
