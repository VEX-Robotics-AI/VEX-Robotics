def when_started():
    # Going to age 28, since it will be the age of a 13 year old in 2035
    # Move forward to go up the tens
    for repeat_count in range(2):
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)
    # turn right to move down the ones digits
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    for repeat_count2 in range(7):
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)

vr_thread(when_started())
