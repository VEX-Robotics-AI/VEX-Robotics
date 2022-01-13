petal = 0

def red_and_black_spiral():
    global petal
    petal = 0
    while not petal > 13:
        pen.set_pen_color(RED)
        for repeat_count in range(10):
            drivetrain.drive_for(FORWARD, 10, MM)
            drivetrain.turn_for(RIGHT, 15, DEGREES)
            wait(5, MSEC)
        pen.set_pen_color(BLACK)
        drivetrain.drive_for(FORWARD, 1000, MM)
        petal = petal + 1
        wait(5, MSEC)

def blue_and_green_spiral():
    global petal
    pen.set_pen_color(BLUE)
    petal = 0
    while not petal > 15:
        if petal % 2 == 0:
            pen.set_pen_color(GREEN)
        else:
            pen.set_pen_color(BLUE)
        for repeat_count2 in range(15):
            drivetrain.drive_for(FORWARD, 10, MM)
            drivetrain.turn_for(RIGHT, 10.5, DEGREES)
            wait(5, MSEC)
        drivetrain.drive_for(FORWARD, 1000, MM)
        petal = petal + 1
        wait(5, MSEC)

def when_started():
    global petal
    drivetrain.drive_for(FORWARD, 500, MM)
    pen.move(DOWN)
    # Draw a blue and green spiral
    blue_and_green_spiral()
    # Draw a red and black spiral
    red_and_black_spiral()

vr_thread(when_started())
