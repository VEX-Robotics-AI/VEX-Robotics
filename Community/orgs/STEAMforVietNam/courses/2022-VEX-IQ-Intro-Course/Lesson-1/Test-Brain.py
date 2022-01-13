"""
On Robot Mesh Studio: https://www.robotmesh.com/studio/60112ff3bf4a15058c6bbeba
"""


# IMPORT CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ================================

from vex import (
    Brain,
    NoteType, SECONDS
)


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo brain
brain = Brain()


# CHƯƠNG TRÌNH CHÍNH
# ==================

while True:
    # nếu phím Check được nhấn thì brain ghi 'CHECK' và phát âm thanh vừa
    if brain.buttonCheck.pressing():
        brain.screen.print_line(1, 'CHECK')

        brain.sound.play(
            NoteType.F,   # note
            4,   # octave
            0.5,   # độ dài thời gian
            SECONDS   # đơn vị thời gian
        )

    # nếu phím Xuống được nhấn thì brain ghi 'DOWN' và phát âm thanh trầm
    elif brain.buttonDown.pressing():
        brain.screen.print_line(1, 'DOWN')

        brain.sound.play(
            NoteType.C,   # note
            4,   # octave
            0.5,   # độ dài thời gian
            SECONDS   # đơn vị thời gian
        )

    # nếu phím Lên được nhấn thì màn hình ghi 'Up' và brain phát âm thanh cao
    elif brain.buttonUp.pressing():
        brain.screen.print_line(1, 'UP')

        brain.sound.play(
            NoteType.B,   # note
            4,   # octave
            0.5,   # độ dài thời gian
            SECONDS   # đơn vị thời gian
        )

    else:
        brain.screen.clear_screen()
