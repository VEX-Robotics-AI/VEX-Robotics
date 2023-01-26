my_variable = 0

def spiral_in():
    global my_variable
    # These blocks program the robot to spiral in on the grid
    my_variable = 1800
    for repeat_count in range(3):
        drivetrain.drive_for(FORWARD, my_variable, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        wait(5, MSEC)
    my_variable = my_variable + -200
    while not my_variable < 200:
        for repeat_count2 in range(2):
            drivetrain.drive_for(FORWARD, my_variable, MM)
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            wait(5, MSEC)
        my_variable = my_variable + -200
        for repeat_count3 in range(2):
            drivetrain.drive_for(FORWARD, my_variable, MM)
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            wait(5, MSEC)
        my_variable = my_variable + -200
        wait(5, MSEC)

def spiral_out():
    global my_variable
    # These blocks program the robot to spiral out
    my_variable = 200
    for repeat_count4 in range(2):
        drivetrain.drive_for(FORWARD, my_variable, MM)
        drivetrain.turn_for(LEFT, 90, DEGREES)
        wait(5, MSEC)
    my_variable = my_variable + 200
    while not my_variable > 1600:
        for repeat_count5 in range(2):
            drivetrain.drive_for(FORWARD, my_variable, MM)
            drivetrain.turn_for(LEFT, 90, DEGREES)
            wait(5, MSEC)
        my_variable = my_variable + 200
        for repeat_count6 in range(2):
            drivetrain.drive_for(FORWARD, my_variable, MM)
            drivetrain.turn_for(LEFT, 90, DEGREES)
            wait(5, MSEC)
        my_variable = my_variable + 200
        wait(5, MSEC)
    drivetrain.drive_for(FORWARD, 1800, MM)

def when_started():
    global my_variable
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    pen.set_pen_color(GREEN)
    pen.move(DOWN)
    # Use the Spiral in function
    spiral_in()
    # Adjusts 10mm to see the outward spiral
    drivetrain.drive_for(FORWARD, 10, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    # Adjusts 10mm again
    drivetrain.drive_for(FORWARD, 10, MM)
    pen.set_pen_color(RED)
    spiral_out()

vr_thread(when_started())
