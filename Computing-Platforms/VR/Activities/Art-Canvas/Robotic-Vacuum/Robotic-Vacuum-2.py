my_distance = 0

def when_started():
    global my_distance
    my_distance = 100
    while True:
        drivetrain.drive(FORWARD)
        while not distance.get_distance(MM) < my_distance:
            wait(5, MSEC)
        drivetrain.turn_for(RIGHT, 110, DEGREES)
        wait(5, MSEC)

vr_thread(when_started())
