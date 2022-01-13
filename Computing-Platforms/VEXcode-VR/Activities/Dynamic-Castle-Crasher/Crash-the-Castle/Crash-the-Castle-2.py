vexcode_brain_precision = 0
castleCount = 0

def find_something():
    global castleCount, vexcode_brain_precision
    drivetrain.turn_for(LEFT, 5, DEGREES)
    while not distance.found_object():
        drivetrain.turn(RIGHT)
        wait(5, MSEC)

def when_started():
    global castleCount, vexcode_brain_precision
    # This solution knocks over all the structures on at least 3 of the Dynamic Castle Crasher Playgrounds
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    castleCount = 15
    while not castleCount < 0:
        drivetrain.drive(FORWARD)
        if left_bumper.pressed() or right_bumper.pressed() or down_eye.detect(RED):
            drivetrain.drive_for(FORWARD, 50, MM)
            drivetrain.drive_for(FORWARD, 200, MM)
            drivetrain.drive_for(REVERSE, 200, MM)
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            find_something()
            castleCount = castleCount + -1
        if not distance.found_object():
            find_something()
        wait(5, MSEC)
    drivetrain.stop()
    brain.print("ALL DONE!")

vr_thread(when_started())
