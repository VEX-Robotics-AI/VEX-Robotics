limit = 0

def when_started():
    global limit
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    while not brain.timer_time(SECONDS) > 400:
        drivetrain.drive(FORWARD)
        while not (math.fabs(location.position(X, MM)) > 800 or math.fabs(location.position(Y, MM)) > 800):
            wait(5, MSEC)
        drivetrain.drive_for(FORWARD, 100, MM)
        drivetrain.drive_for(REVERSE, 500, MM)
        drivetrain.turn(RIGHT)
        limit = 1500
        while not distance.get_distance(MM) < limit:
            wait(5, MSEC)
        drivetrain.turn_for(RIGHT, 2, DEGREES)
        limit = limit + -5
        drivetrain.drive(FORWARD)
        wait(5, MSEC)
    drivetrain.stop()

vr_thread(when_started())
