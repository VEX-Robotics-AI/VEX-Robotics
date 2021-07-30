def when_started():
    # going to age 13
    # Move forward to go up the tens
    for repeat_count in range(1):
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)
    # turn right to move down the ones digits
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    for repeat_count2 in range(2):
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)

vr_thread(when_started())
