def drive_until_red():
    drivetrain.drive(FORWARD)
    while not down_eye.detect(RED):
        wait(5, MSEC)

def when_started():
    # Sets drive faster, but not too fast
    drivetrain.set_drive_velocity(60, PERCENT)
    drivetrain.turn_to_heading(90, DEGREES)
    drive_until_red()
    drivetrain.turn_to_heading(350, DEGREES)
    drive_until_red()
    drivetrain.turn_to_heading(215, DEGREES)
    drive_until_red()
    drivetrain.turn_to_heading(0, DEGREES)
    drive_until_red()
    drivetrain.turn_to_heading(270, DEGREES)
    drive_until_red()
    drivetrain.turn_to_heading(180, DEGREES)
    drive_until_red()
    drivetrain.stop()

vr_thread(when_started())
