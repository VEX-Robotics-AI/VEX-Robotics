my_variable = 0

def when_started():
    global my_variable
    pen.move(DOWN)
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

vr_thread(when_started())
