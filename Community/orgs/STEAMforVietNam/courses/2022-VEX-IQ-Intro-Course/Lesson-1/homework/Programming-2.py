# NHẬP CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ==============================

#################################################################
# 1) Hãy nhập các lớp (class) Brain và NoteType từ thư viện vex #
#################################################################
from vex import Brain, NoteType


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

###################################
# 2) Hãy khởi tạo đối tượng brain #
###################################
brain = Brain()


# CHƯƠNG TRÌNH CHÍNH
# ==================

###############################################################################
# 3) Hãy dùng hàm (method) .play(...) của thuộc tính (attribute) brain.sound  #
# của đối tượng brain để chơi nốt nhạc NoteType.C                             #
#                                                                             #
#    Chú ý:                                                                   #
#    - brain.sound là một instance thuộc lớp (class) BrainSound               #
#    - hãy đọc hướng dẫn API của các lớp Brain, BrainSound và NoteType        #
#      qua Robot Mesh Studio Help                                             #
###############################################################################
brain.sound.play(NoteType.C)
