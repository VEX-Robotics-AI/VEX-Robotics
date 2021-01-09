def when_started():
    # Turn right to go down the X axis
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(X, MM) >= -500:
        wait(5, MSEC)
    drivetrain.stop()
    # Turn left to go up the Y axis
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) >= 700:
        wait(5, MSEC)
    drivetrain.stop()

vr_thread(when_started())
