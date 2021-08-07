"""
http://bit.ly/S4V_CS201_For_Loop
https://www.robotmesh.com/studio/60bd45e24271ec49ce231d47
"""


gio_hang = ['tao', 'cam', 'quyt']

# Dùng vòng lặp for để lặp qua từng phần tử của danh sách
# for item in gio_hang:
#     print('Trong gio hang co: ' + item)

# ===============================================
# Ứng dụng: tính tuổi trung bình của nhóm học sinh
nhom_1 = [['Nga', 10], ['Quang', 8], ['Vinh', 13], ['Minh', 9]]

tong = 0

for phan_tu in nhom_1:
    tuoi = phan_tu[1]
    tong += tuoi   # tong = tong + tuoi

print(tong)
print(tong / len(nhom_1))
