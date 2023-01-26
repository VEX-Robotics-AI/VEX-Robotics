petal = 0

def when_started():
    global petal
    drivetrain.set_turn_velocity(100, PERCENT)
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.drive_for(FORWARD, 500, MM)
    pen.move(DOWN)
    petal = 0
    while not petal > 15:
        for repeat_count in range(15):
            drivetrain.drive_for(FORWARD, 10, MM)
            drivetrain.turn_for(RIGHT, 10.5, DEGREES)
            wait(5, MSEC)
        drivetrain.drive_for(FORWARD, 1000, MM)
        petal = petal + 1
        wait(5, MSEC)

vr_thread(when_started())
