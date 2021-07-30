def draw_square():
    drivetrain.drive_for(FORWARD, 100, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 100, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    pen.move(DOWN)
    pen.set_pen_color(BLUE)
    # moved 1600 mm
    for repeat_count in range(8):
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    # moved 1600 mm
    for repeat_count2 in range(8):
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    # moved 1600 mm
    for repeat_count3 in range(8):
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    # moved 1600 mm
    for repeat_count4 in range(8):
        drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    # perimeter: 6400 mm
    pen.move(UP)

def when_started():
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    draw_square()
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 600, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    pen.move(DOWN)
    pen.set_pen_color(RED)
    for repeat_count6 in range(4):
        for repeat_count5 in range(3):
            drivetrain.drive_for(FORWARD, 200, MM)
            drivetrain.turn_for(LEFT, 90, DEGREES)
            drivetrain.drive_for(FORWARD, 200, MM)
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            wait(5, MSEC)
        drivetrain.drive_for(FORWARD, 400, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        wait(5, MSEC)

vr_thread(when_started())
