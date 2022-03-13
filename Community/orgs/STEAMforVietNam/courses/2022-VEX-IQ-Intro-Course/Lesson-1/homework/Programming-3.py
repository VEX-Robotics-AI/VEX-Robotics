"""
1) Hãy nhập từ thư viện vex:
- các lớp (class) Motor và Ports
- đơn vị DEGREES
- các hằng số hướng quay FORWARD và REVERSE

2) Hãy khởi tạo một motor nối với cổng PORT1

3) Hãy dùng hàm (method) .spin_for(...) của đối tượng motor để:
- quay motor xuôi chiều 180 độ, rồi
- quay motor ngược chiều 360 độ

Chú ý: hãy đọc hướng dẫn API của lớp Motor qua Robot Mesh Studio Help
"""


# NHẬP CÁC ĐỐI TƯỢNG TỪ THƯ VIỆN
# ==============================

###############################################
# 1) Hãy nhập từ thư viện vex:                #
# - các lớp (class) Motor và Ports            #
# - đơn vị DEGREES                            #
# - các hằng số hướng quay FORWARD và REVERSE #
###############################################
from vex import Motor, Ports, DEGREES, FORWARD, REVERSE


# KHỞI TẠO CÁC BỘ PHẬN ROBOT
# ==========================

################################################
# 2) Hãy khởi tạo một motor nối với cổng PORT1 #
################################################
motor = Motor(Ports.PORT1)


# CHƯƠNG TRÌNH CHÍNH
# ==================

###############################################################################
# 3) Hãy dùng hàm (method) .spin_for(...) của đối tượng motor để:             #
#    - quay motor xuôi chiều 180 độ, rồi                                      #
#    - quay motor ngược chiều 360 độ                                          #
#                                                                             #
#    Chú ý: hãy đọc hướng dẫn API của lớp Motor qua Robot Mesh Studio Help    #
###############################################################################
motor.spin_for(FORWARD, 180, DEGREES)
motor.spin_for(REVERSE, 360, DEGREES)
