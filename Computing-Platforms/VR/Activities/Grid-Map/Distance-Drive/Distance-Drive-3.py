def when_started():
    for repeat_count in range(4):
        drivetrain.drive_for(FORWARD, 400, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        wait(5, MSEC)

vr_thread(when_started())
