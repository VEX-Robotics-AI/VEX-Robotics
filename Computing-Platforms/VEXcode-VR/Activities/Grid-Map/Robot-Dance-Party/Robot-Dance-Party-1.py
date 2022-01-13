def when_started():
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    # Move out to the dance floor...
    for repeat_count in range(10):
        drivetrain.drive_for(FORWARD, 100, MM)
        drivetrain.turn_for(RIGHT, 10, DEGREES)
        wait(5, MSEC)
    drivetrain.turn_to_heading(0, DEGREES)
    # Put your right wheel in...
    drivetrain.turn_for(LEFT, 20, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    # Take your right wheel out...
    drivetrain.drive_for(REVERSE, 200, MM)
    wait(0.5, SECONDS)
    drivetrain.drive_for(FORWARD, 200, MM)
    # Shake it all about...
    for repeat_count2 in range(10):
        drivetrain.turn_for(RIGHT, 10, DEGREES)
        drivetrain.turn_for(LEFT, 10, DEGREES)
        wait(5, MSEC)
    drivetrain.drive_for(REVERSE, 200, MM)
    # Turn yourself around...
    drivetrain.turn_for(RIGHT, 380, DEGREES)

vr_thread(when_started())
