def until_red():
    drivetrain.drive(FORWARD)
    while not down_eye.detect(RED):
        wait(5, MSEC)
    drivetrain.drive_for(REVERSE, 50, MM)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.drive_for(REVERSE, 500, MM)
    drivetrain.stop()

def when_started():
    drivetrain.set_drive_velocity(100, PERCENT)
    while True:
        if distance.found_object():
            until_red()
        else:
            drivetrain.turn(RIGHT)
        wait(5, MSEC)

vr_thread(when_started())
