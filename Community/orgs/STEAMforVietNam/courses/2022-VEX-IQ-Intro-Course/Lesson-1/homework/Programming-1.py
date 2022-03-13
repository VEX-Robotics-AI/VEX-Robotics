"""
1. Hãy nhập lớp (class) Brain từ thư viện vex

2. Hãy khởi tạo đối tượng brain

3. Hãy dùng hàm (method) .print_line(...)
của thuộc tính (attribute) brain.screen của đối tượng brain
để in 'STEAM for Vietnam' tại dòng số 3 của màn hình LCD của brain

Chú ý:
- brain.screen là một instance thuộc lớp (class) BrainLcd
- hãy đọc hướng dẫn API của các lớp Brain & BrainLcd qua Robot Mesh Studio Help
"""


# NHẬP CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ==============================

#################################################
# 1) Hãy nhập lớp (class) Brain từ thư viện vex #
#################################################
from vex import Brain


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

###################################
# 2) Hãy khởi tạo đối tượng brain #
###################################
brain = Brain()


# CHƯƠNG TRÌNH CHÍNH
# ==================

###############################################################################
# 3) Hãy dùng hàm (method) .print_line(...)                                   #
# của thuộc tính (attribute) brain.screen của đối tượng brain                 #
# để in 'STEAM for Vietnam' tại dòng số 3 của màn hình LCD của brain          #
#                                                                             #
#    Chú ý:                                                                   #
#    - brain.screen là một instance thuộc lớp (class) BrainLcd                #
#    - hãy đọc hướng dẫn API của các lớp Brain & BrainLcd                     #
#      qua Robot Mesh Studio Help                                             #
###############################################################################
brain.screen.print_line(3, 'STEAM for Vietnam')
