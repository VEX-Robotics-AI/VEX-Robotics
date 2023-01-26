def when_started():
    # Blue Disk
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.drive_for(FORWARD, 800, MM)
    magnet.energize(BOOST)
    drivetrain.drive_for(REVERSE, 800, MM)
    magnet.energize(DROP)
    # Red Disk
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 800, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 800, MM)
    magnet.energize(BOOST)
    drivetrain.drive_for(REVERSE, 800, MM)
    magnet.energize(DROP)
    # Green Disk
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 800, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 800, MM)
    magnet.energize(BOOST)
    drivetrain.drive_for(REVERSE, 800, MM)
    magnet.energize(DROP)

vr_thread(when_started())
