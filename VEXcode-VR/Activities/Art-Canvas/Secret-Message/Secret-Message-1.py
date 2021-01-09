x1 = 0
x2 = 0
y2 = 0
y1 = 0
result_angle = 0
distance_result = 0
counter_var = 0
less_than_zero = False
first_set = [[0 for y in range(10)] for x in range(3)]
second_set = [[0 for y in range(10)] for x in range(3)]

def when_started():
    global x1, x2, y2, y1, result_angle, distance_result, counter_var, less_than_zero, first_set, second_set
    drivetrain.set_turn_velocity(100, PERCENT)
    drivetrain.set_drive_velocity(100, PERCENT)
    # Step 1.
    drivetrain.turn_to_heading(296.56, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) > 400:
        wait(5, MSEC)
    # Step 2.
    pen.move(DOWN)
    # Step 3.
    drivetrain.turn_to_heading(165.96, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) < -400:
        wait(5, MSEC)
    # Step 4.
    drivetrain.turn_to_heading(14.4, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) > 400:
        wait(5, MSEC)
    # Step 5.
    pen.move(UP)
    # Step 6.
    drivetrain.turn_to_heading(90, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(X, MM) > -200:
        wait(5, MSEC)
    # Step 7.
    pen.move(DOWN)
    # Step 8.
    drivetrain.drive(FORWARD)
    while not location.position(X, MM) > 200:
        wait(5, MSEC)
    # Step 9.
    pen.move(UP)
    # Step 10.
    drivetrain.drive(REVERSE)
    while not location.position(X, MM) < -200:
        wait(5, MSEC)
    drivetrain.turn_to_heading(180, DEGREES)
    # Step 11.
    pen.move(DOWN)
    # Step 12.
    drivetrain.drive_for(FORWARD, 800, MM)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) > 0:
        wait(5, MSEC)
    # Step 13.
    pen.move(UP)
    # Step 14.
    drivetrain.turn_to_heading(90, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(X, MM) > 200:
        wait(5, MSEC)
    # Step 15.
    pen.move(DOWN)
    # Step 16.
    drivetrain.drive(REVERSE)
    while not location.position(X, MM) < -200:
        wait(5, MSEC)
    # Step 17.
    pen.move(UP)
    # Step 18.
    drivetrain.turn_to_heading(180, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) < -400:
        wait(5, MSEC)
    # Step 19.
    pen.move(DOWN)
    # Step 20.
    drivetrain.turn_to_heading(90, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(X, MM) > 200:
        wait(5, MSEC)
    # Step 21.
    pen.move(UP)
    # Step 22.
    drivetrain.turn_to_heading(14.03, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) > 400:
        wait(5, MSEC)
    # Step 23.
    pen.move(DOWN)
    # Step 24.
    drivetrain.turn_to_heading(153.44, DEGREES)
    # Step 25.
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) < -400:
        wait(5, MSEC)
    # Step 26.
    pen.move(UP)
    # Step 27.
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) > 400:
        wait(5, MSEC)
    # Step 28.
    pen.move(DOWN)
    # Step 29.
    drivetrain.turn_to_heading(206.57, DEGREES)
    drivetrain.drive(FORWARD)
    # Step 30.
    while not location.position(Y, MM) < -400:
        wait(5, MSEC)
    # Step 31.
    pen.move(UP)
    # You've uncovered the secret message!
    drivetrain.stop()

vr_thread(when_started())
