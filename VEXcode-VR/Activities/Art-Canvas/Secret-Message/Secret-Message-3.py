x1 = 0
x2 = 0
y2 = 0
y1 = 0
result_angle = 0
distance_result = 0
counter_var = 0
less_than_zero = False
first_set = [[0 for y in range(10)] for x in range(3)]
second_set = [[0 for y in range(10)] for x in range(3)]

def move_and_set_pen(x_coordinate, y_coordinate, pen_state):
    global x1, x2, y2, y1, result_angle, distance_result, counter_var, less_than_zero, first_set, second_set
    if pen_state == 1:
        pen.move(DOWN)
    else:
        pen.move(UP)
    # Starting Point
    x1 = location.position(X, MM)
    y1 = location.position(Y, MM)
    # Destination Point
    x2 = x_coordinate
    y2 = y_coordinate
    # Logic to implement ATAN2
    less_than_zero = y2 - y1 < 0
    if y2 == y1:
        if x2 > x1:
            result_angle = 90
        else:
            result_angle = 270
    else:
        if less_than_zero:
            result_angle = math.atan((x2 - x1) / (y2 - y1)) / math.pi * 180 + 180
        else:
            result_angle = math.atan((x2 - x1) / (y2 - y1)) / math.pi * 180
    drivetrain.turn_to_heading(result_angle, DEGREES)
    # Calculate distance to travel
    distance_result = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
    drivetrain.drive_for(FORWARD, distance_result, MM)

def when_started1():
    global x1, x2, y2, y1, result_angle, distance_result, counter_var, less_than_zero, first_set, second_set
    first_set = [
        [0, -800, 400],
        [1, -600, -400],
        [1, -400, 400],
        [0, -200, 400],
        [1, 200, 400],
        [0, -200, 400],
        [1, -200, -400],
        [0, -200, 0],
        [1, 200, 0],
        [0, -200, -400]
    ]
    second_set = [
        [1, 200, -400],
        [0, 400, 400],
        [1, 600, 0],
        [1, 800, -400],
        [0, 800, 400],
        [1, 600, 0],
        [1, 400, -400],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    counter_var = 1
    for repeat_count in range(10):
        move_and_set_pen(first_set[counter_var - 1][2 - 1], first_set[counter_var - 1][3 - 1], first_set[counter_var - 1][1 - 1])
        counter_var = counter_var + 1
        wait(5, MSEC)
    counter_var = 1
    for repeat_count2 in range(10):
        move_and_set_pen(second_set[counter_var - 1][2 - 1], second_set[counter_var - 1][3 - 1], second_set[counter_var - 1][1 - 1])
        counter_var = counter_var + 1
        wait(5, MSEC)

vr_thread(when_started1())
