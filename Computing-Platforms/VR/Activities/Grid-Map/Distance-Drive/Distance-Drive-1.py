def when_started():
    drivetrain.drive_for(FORWARD, 600, MM)

vr_thread(when_started())
