wall = False
all_done = False

def drive_forward():
    global wall, all_done
    wall = False
    drivetrain.drive_for(FORWARD, 250, MM, wait=False)
    wait(1, SECONDS)
    while not (wall or all_done or drivetrain.is_done()):
        # did I hit a wall
        if left_bumper.pressed() and right_bumper.pressed():
            drivetrain.stop()
            wall = True
        # are we done?
        if down_eye.detect(RED):
            all_done = True
        wait(5, MSEC)

def when_started():
    global wall, all_done
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    all_done = False
    wall = False
    # Turn Right Algorithm
    while True:
        if wall:
            drivetrain.turn_for(LEFT, 90, DEGREES)
            drive_forward()
        else:
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            drive_forward()
        # If Done spin in place forever
        if all_done:
            break
        wait(5, MSEC)
    drivetrain.stop()

vr_thread(when_started())
