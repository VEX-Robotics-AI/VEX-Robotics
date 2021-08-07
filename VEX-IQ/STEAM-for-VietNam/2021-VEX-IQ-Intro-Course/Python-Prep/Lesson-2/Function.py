"""
http://bit.ly/S4V_CS201_Function
https://www.robotmesh.com/studio/60bd54d55ba6e20556d7ed12
"""


# Vi du 1
# ===============================================

led_status = [0, 0, 0, 0]


# def ten_ham(tham_so):
def turn_led_on(led_num):
    led_status[led_num] = 1
    print('LED ' + str(led_num) + ' turned on')

# turn_led_on(0)
# turn_led_on(3)
# print(led_status)


# Vi du 2
# ===============================================

led_status = [0, 0, 0, 0]


def how_many_led_on():
    on_total = 0
    for led in led_status:
        if led == 1:
            on_total += 1
    return on_total


led_on_count = how_many_led_on()
print(led_on_count)

turn_led_on(1)
turn_led_on(3)
print("Da bat den: ")
print(how_many_led_on())
