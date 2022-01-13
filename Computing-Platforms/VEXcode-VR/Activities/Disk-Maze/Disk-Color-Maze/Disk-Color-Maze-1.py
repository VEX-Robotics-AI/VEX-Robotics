def when_started():
    while True:
        if front_eye.near_object():
            if front_eye.detect(GREEN):
                drivetrain.turn_for(RIGHT, 90, DEGREES)
            if front_eye.detect(BLUE):
                drivetrain.turn_for(LEFT, 90, DEGREES)
            if front_eye.detect(RED):
                drivetrain.stop()
        else:
            drivetrain.drive(FORWARD)
        wait(5, MSEC)

vr_thread(when_started())
