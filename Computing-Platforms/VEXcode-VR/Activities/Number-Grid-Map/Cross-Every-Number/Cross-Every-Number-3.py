Counter = 0

def when_started():
    global Counter
    # The counter variable will help us keep track of how many times we have gone through the loop.
    Counter = 0
    for repeat_count2 in range(10):
        Counter = Counter + 1
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        pen.move(DOWN)
        pen.set_pen_color(RED)
        drivetrain.drive_for(FORWARD, 100, MM)
        for repeat_count in range(4):
            pen.set_pen_color(BLUE)
            drivetrain.drive_for(FORWARD, 200, MM)
            pen.set_pen_color(RED)
            drivetrain.drive_for(FORWARD, 200, MM)
            wait(5, MSEC)
        pen.set_pen_color(BLUE)
        drivetrain.drive_for(FORWARD, 100, MM)
        pen.move(UP)
        # Once we have looped 10 times, we will prevent the robot from trying to move up to another line.
        if Counter < 10:
            drivetrain.drive_for(REVERSE, 1800, MM)
            drivetrain.turn_for(LEFT, 90, DEGREES)
            drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)

vr_thread(when_started())
