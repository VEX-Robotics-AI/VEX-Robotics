start_x = 0
destination_x = 0
destination_y = 0
start_y = 0
turn_for = 0
drive_distance = 0
limit = 0
cube_count = 0
less_than_zero = False

def sweep():
    global start_x, destination_x, destination_y, start_y, turn_for, drive_distance, limit, cube_count, less_than_zero
    # Creates conditions so the robot does not keep looking for blocks to push off forever
    while not (limit > 810 or math.fabs(drivetrain.rotation(DEGREES)) > 2500):
        # Slows the robot down near the edge and gives blocks a little nudge so they fall off but VR does not
        if math.fabs(location.position(X, MM)) > 680 or math.fabs(location.position(Y, MM)) > 680:
            drivetrain.set_drive_velocity(35, PERCENT)
            drivetrain.set_turn_velocity(35, PERCENT)
            drivetrain.drive_for(REVERSE, 25, MM)
            drivetrain.drive_for(FORWARD, 100, MM)
            drivetrain.drive_for(REVERSE, 70, MM)
        # Makes the perimeter limit a little bigger each time the loop runs
        limit = limit + 5
        drivetrain.set_drive_velocity(80, PERCENT)
        drivetrain.set_turn_velocity(45, PERCENT)
        move_to(0, 0)
        # Turns left until an object is detected or the absolute value of rotation degrees is less than -300
        drivetrain.turn(RIGHT)
        while not (distance.get_distance(MM) < limit + limit * 0.2 or drivetrain.rotation(DEGREES) > -300):
            wait(5, MSEC)
        drivetrain.set_drive_velocity(75, PERCENT)
        # This nested loop runs until it reaches the slowly-expanding perimeter limit
        while not (math.fabs(location.position(X, MM)) > limit or math.fabs(location.position(Y, MM)) > limit):
            if math.fabs(location.position(X, MM)) < limit and math.fabs(location.position(Y, MM)) < limit:
                drivetrain.drive(FORWARD)
                # Chases after blocks if bumpers detect them
                if left_bumper.pressed() and not right_bumper.pressed():
                    drivetrain.turn(LEFT)
                if right_bumper.pressed() and not left_bumper.pressed():
                    drivetrain.turn(RIGHT)
                if not distance.found_object() or distance.get_distance(MM) > limit + 50:
                    drivetrain.turn(LEFT)
            wait(5, MSEC)
        wait(5, MSEC)
    move_to(0, 0)

def sweep_perimeter():
    global start_x, destination_x, destination_y, start_y, turn_for, drive_distance, limit, cube_count, less_than_zero
    drivetrain.set_drive_velocity(80, PERCENT)
    move_to(875, 875)
    move_to(-880, 900)
    move_to(-900, -900)
    move_to(900, -900)
    move_to(900, 900)
    move_to(0, 0)

def move_to(x_coordinate, y_coordinate):
    global start_x, destination_x, destination_y, start_y, turn_for, drive_distance, limit, cube_count, less_than_zero
    start_x = location.position(X, MM)
    start_y = location.position(Y, MM)
    # Destination Point
    destination_x = x_coordinate
    destination_y = y_coordinate
    # Logic to implement ATAN2
    less_than_zero = destination_y - start_y < 0
    if less_than_zero:
        turn_for = math.atan((destination_x - start_x) / (destination_y - start_y)) / math.pi * 180 + 180
    else:
        turn_for = math.atan((destination_x - start_x) / (destination_y - start_y)) / math.pi * 180
    drivetrain.turn_to_heading(turn_for, DEGREES)
    # Calculate distance to travel
    drive_distance = math.sqrt((destination_x - start_x) * (destination_x - start_x) + (destination_y - start_y) * (destination_y - start_y))
    drivetrain.drive_for(FORWARD, drive_distance, MM)

def when_started():
    global start_x, destination_x, destination_y, start_y, turn_for, drive_distance, limit, cube_count, less_than_zero
    drivetrain.set_drive_velocity(95, PERCENT)
    # Uses our move_to_x_y function to crash outer castles
    move_to(-870, 900)
    move_to(900, -900)
    move_to(750, 900)
    move_to(-850, -900)
    limit = 755
    sweep()
    # Sweeps blocks caught on the edge
    sweep_perimeter()

vr_thread(when_started())
