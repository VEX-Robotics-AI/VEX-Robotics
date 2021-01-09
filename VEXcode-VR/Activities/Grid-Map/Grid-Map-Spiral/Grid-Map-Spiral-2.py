my_variable = 0

def check_direction(number):
    global my_variable
    if 0 <= number <= 0.01:
        pen.set_pen_color(RED)
    if 89.9 <= number <= 90.1:
        pen.set_pen_color(GREEN)
    if 179.99 <= number <= 180.01:
        pen.set_pen_color(BLUE)
    if 269.99 <= number <= 270.01:
        pen.set_pen_color(BLACK)

def when_started():
    global my_variable
    pen.move(DOWN)
    my_variable = 1800
    for repeat_count in range(3):
        check_direction(drivetrain.heading(DEGREES))
        drivetrain.drive_for(FORWARD, my_variable, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        wait(5, MSEC)
    my_variable = my_variable + -200
    while not my_variable < 200:
        for repeat_count2 in range(2):
            check_direction(drivetrain.heading(DEGREES))
            drivetrain.drive_for(FORWARD, my_variable, MM)
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            wait(5, MSEC)
        my_variable = my_variable + -200
        for repeat_count3 in range(2):
            check_direction(drivetrain.heading(DEGREES))
            drivetrain.drive_for(FORWARD, my_variable, MM)
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            wait(5, MSEC)
        my_variable = my_variable + -200
        wait(5, MSEC)

vr_thread(when_started())
