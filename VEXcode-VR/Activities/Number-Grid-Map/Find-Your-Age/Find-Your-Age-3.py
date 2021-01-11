old_heading = 0

def mark_square_red():
    global old_heading
    old_heading = drivetrain.heading(DEGREES)
    drivetrain.turn_to_heading(180, DEGREES)
    pen.move(DOWN)
    pen.set_pen_color(RED)
    drivetrain.drive_for(FORWARD, 5, MM)
    drivetrain.drive_for(REVERSE, 10, MM)
    drivetrain.drive_for(FORWARD, 5, MM)
    pen.move(UP)
    drivetrain.turn_to_heading(old_heading, DEGREES)

def mark_square_blue():
    global old_heading
    old_heading = drivetrain.heading(DEGREES)
    drivetrain.turn_to_heading(180, DEGREES)
    pen.move(DOWN)
    pen.set_pen_color(BLUE)
    drivetrain.drive_for(FORWARD, 5, MM)
    drivetrain.drive_for(REVERSE, 10, MM)
    drivetrain.drive_for(FORWARD, 5, MM)
    pen.move(UP)
    drivetrain.turn_to_heading(old_heading, DEGREES)

def mark_square_green():
    global old_heading
    old_heading = drivetrain.heading(DEGREES)
    drivetrain.turn_to_heading(180, DEGREES)
    pen.move(DOWN)
    pen.set_pen_color(GREEN)
    drivetrain.drive_for(FORWARD, 5, MM)
    drivetrain.drive_for(REVERSE, 10, MM)
    drivetrain.drive_for(FORWARD, 5, MM)
    pen.move(UP)
    drivetrain.turn_to_heading(old_heading, DEGREES)

def when_started():
    global old_heading
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    # Moving to the VR's birthday, 04/02/2020
    # month
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    for repeat_count in range(3):
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    for repeat_count2 in range(0):
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)
    mark_square_red()
    # day
    drivetrain.turn_for(LEFT, 90, DEGREES)
    for repeat_count3 in range(2):
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    for repeat_count4 in range(0):
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)
    mark_square_blue()
    drivetrain.turn_for(LEFT, 90, DEGREES)
    for repeat_count5 in range(8):
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)
    # turn left to move up tens digits
    drivetrain.turn_for(LEFT, 90, DEGREES)
    for repeat_count6 in range(1):
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)
    mark_square_green()
    # drive forward to show all marks
    drivetrain.drive_for(FORWARD, 200, MM)

vr_thread(when_started())
