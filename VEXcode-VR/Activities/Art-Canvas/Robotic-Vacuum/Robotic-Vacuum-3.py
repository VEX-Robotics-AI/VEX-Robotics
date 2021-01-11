dist = 0

def when_started():
    global dist
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    dist = 120
    pen.move(DOWN)
    while True:
        drivetrain.drive(FORWARD)
        while not distance.get_distance(MM) < dist:
            wait(5, MSEC)
        drivetrain.turn_for(RIGHT, random.randint((90 - 1), 180), DEGREES)
        wait(5, MSEC)

vr_thread(when_started())
