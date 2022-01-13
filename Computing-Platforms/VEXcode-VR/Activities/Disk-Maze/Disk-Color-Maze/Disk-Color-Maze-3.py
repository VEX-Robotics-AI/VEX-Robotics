my_variable = 0
green_disk = 0

def detect_color_square(square):
    global my_variable, green_disk
    drivetrain.drive(FORWARD)
    wait(0.2, SECONDS)
    while not (down_eye.detect(GREEN) or down_eye.detect(BLUE)):
        wait(5, MSEC)
    if down_eye.detect(GREEN):
        if square:
            drivetrain.drive(FORWARD)
            while not not down_eye.detect(GREEN):
                wait(5, MSEC)
            drivetrain.drive_for(FORWARD, 50, MM)
        drivetrain.turn_for(LEFT, 90, DEGREES)
    else:
        if down_eye.detect(BLUE):
            if square:
                drivetrain.drive(FORWARD)
                while not not down_eye.detect(BLUE):
                    wait(5, MSEC)
                drivetrain.drive_for(FORWARD, 50, MM)
            drivetrain.turn_for(RIGHT, 90, DEGREES)

def when_started():
    global my_variable, green_disk
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    drivetrain.drive_for(FORWARD, 120, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive(FORWARD)
    while not down_eye.detect(RED):
        wait(5, MSEC)
    drivetrain.drive(FORWARD)
    while not not down_eye.detect(RED):
        wait(5, MSEC)
    drivetrain.drive_for(FORWARD, 50, MM)
    drivetrain.stop()
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive(FORWARD)
    for repeat_count in range(3):
        detect_color_square(False)
        wait(5, MSEC)
    for repeat_count2 in range(3):
        detect_color_square(True)
        wait(5, MSEC)
    for repeat_count3 in range(2):
        detect_color_square(False)
        wait(5, MSEC)
    drivetrain.drive_for(FORWARD, 750, MM)

vr_thread(when_started())
