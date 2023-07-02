"""drive.google.com/file/d/11UUK3HgLWrsIjK_JNW8YvMs5-3_XiRxR"""


# IMPORT FROM LIBRARY
# ===================

from vex import (
    wait,
    SECONDS,
)


# RUN MAIN PROGRAM
# ================

# wait(TIME=3, UNITS=SECONDS)  # DOES NOT COMPILE
# wait(DURATION=3, UNITS=SECONDS)  # DOES NOT COMPILE
# wait(duration=3, units=SECONDS)  # compiles, DOES NOT RUN
# wait(3, units=SECONDS)  # compiles, DOES NOT RUN
wait(3, SECONDS)  # compiles & runs
