def when_started():
    while True:
        drivetrain.drive(FORWARD)
        while not distance.get_distance(MM) < 100:
            wait(5, MSEC)
        drivetrain.turn_for(RIGHT, 110, DEGREES)
        wait(5, MSEC)

vr_thread(when_started())
