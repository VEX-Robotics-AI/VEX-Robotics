wall = False

def drive_forward():
    global wall
    wall = False
    if distance.get_distance(MM) > 250:
        drivetrain.drive_for(FORWARD, 250, MM)
    else:
        wall = True

def when_started():
    global wall
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    wall = False
    # Turn right algorithm
    while not down_eye.detect(RED):
        if wall:
            drivetrain.turn_for(LEFT, 90, DEGREES)
            drive_forward()
        else:
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            drive_forward()
        wait(5, MSEC)
    drivetrain.stop()

vr_thread(when_started())
