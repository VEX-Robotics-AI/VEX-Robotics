"""
On Robot Mesh Studio: https://www.robotmesh.com/studio/60202f736a963405b8ebe1bb
"""


# IMPORT CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ================================

from vex import Brain, wait


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

# khởi tạo brain
brain = Brain()


# CHƯƠNG TRÌNH CHÍNH
# ==================

# in 'Hello World!' tại dòng số 1 của màn hình
# rồi xóa sau vài giây
brain.screen.print_line(1, 'Hello World!')
wait(3)
brain.screen.clear_screen()
