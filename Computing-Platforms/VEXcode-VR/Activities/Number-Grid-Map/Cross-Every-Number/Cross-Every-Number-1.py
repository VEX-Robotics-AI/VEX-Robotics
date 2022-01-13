Counter = 0

def when_started():
    global Counter
    # The counter variable will help us keep track of how many times we have gone through the loop.
    Counter = 0
    pen.move(DOWN)
    for repeat_count in range(5):
        Counter = Counter + 1
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 1800, MM)
        drivetrain.turn_for(LEFT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 200, MM)
        drivetrain.turn_for(LEFT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 1800, MM)
        # Once we have looped 5 times, we will prevent the robot from trying to move up to another line.
        if Counter < 5:
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            drivetrain.drive_for(FORWARD, 200, MM)
        wait(5, MSEC)

vr_thread(when_started())
