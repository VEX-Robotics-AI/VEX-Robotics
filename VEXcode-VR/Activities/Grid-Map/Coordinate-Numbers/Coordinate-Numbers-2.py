def go_to_coordinates(coordinate_X, coordinate_Y):
    # Turn right to go down the X axis
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(X, MM) >= coordinate_X:
        wait(5, MSEC)
    drivetrain.stop()
    # Turn left to go up the Y axis
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) >= coordinate_Y:
        wait(5, MSEC)
    drivetrain.stop()

def when_started():
    # Pass each of the values here
    # (-300mm, -900mm) = 4
    # (700mm, 700mm) = 89
    # (-100mm, 900mm) = 95
    # (500mm, -300mm) = 38
    go_to_coordinates(-300, -900)

vr_thread(when_started())
