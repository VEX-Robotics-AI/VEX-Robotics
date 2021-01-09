gridblocks = 0

def when_started():
    global gridblocks
    gridblocks = 1
    for repeat_count in range(8):
        drivetrain.drive_for(FORWARD, (200 * gridblocks), MM)
        drivetrain.drive_for(REVERSE, (200 * gridblocks), MM)
        gridblocks = gridblocks + 1
        wait(5, MSEC)

vr_thread(when_started())
