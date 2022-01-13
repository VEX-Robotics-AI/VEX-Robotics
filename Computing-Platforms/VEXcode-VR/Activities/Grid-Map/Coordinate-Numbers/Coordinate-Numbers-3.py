def when_started():
    # Turn right to go down the X axis
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive(FORWARD)
    # Change -700 to 500 for 38
    # Change -700 to -300 for 64
    # Change -700 to -100 for 85
    while not location.position(X, MM) >= -700:
        wait(5, MSEC)
    drivetrain.stop()
    # Turn left to go up the Y axis
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive(FORWARD)
    # Change -500 to -300 for 38
    # Change -500 to 300 for 64
    # Change -500 to 700 for 85
    while not location.position(Y, MM) >= -500:
        wait(5, MSEC)
    drivetrain.stop()

vr_thread(when_started())
