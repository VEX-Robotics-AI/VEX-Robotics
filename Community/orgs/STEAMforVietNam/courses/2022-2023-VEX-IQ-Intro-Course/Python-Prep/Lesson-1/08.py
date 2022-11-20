distance = 10
speed = 10
if distance < 10:
    speed = 5
    print('Move slowly')
elif distance < 20:
    speed = 10
    print('Move at right speed')
else:
    speed = 20
    print('Move fast')
