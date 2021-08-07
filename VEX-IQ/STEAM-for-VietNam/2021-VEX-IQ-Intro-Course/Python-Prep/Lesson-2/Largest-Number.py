"""
http://bit.ly/S4V_Largest_Number
https://www.robotmesh.com/studio/60bd40a55ba6e20556d7ecd6

Đề bài: Cho 1 danh sách thành viên nhóm

Tìm người có tuổi lớn nhất của nhóm
Tìm tuổi trung bình của nhóm
"""


print('')
print('')
print('=== Bắt đầu chương trình ===')

# Tạo một danh sách các thành viên trong nhóm
# Trong đó, mỗi thành viên lại cũng là 1 danh sách:
# phần tử 0 --> tên, phần tử 1 --> tuổi
nhom_1 = [['Nga', 10], ['Quang', 8], ['Vinh', 13], ['Minh', 9]]
print('Danh sách nhóm 1: ' + str(nhom_1))

# Hàm len (tức là length): độ dài (số phần tử) của danh sách
so_ban = len(nhom_1)
print('Nhóm có ' + str(so_ban) + ' thành viên')

i = 0
tong_tuoi = 0
tuoi_lon_nhat = 0

# vòng lặp qua từng thành viên nhóm
while i < so_ban:
    thanh_vien = nhom_1[i]
    tuoi_thanh_vien = thanh_vien[1]   # ten = thanh_vien[0]
    tong_tuoi = tong_tuoi + tuoi_thanh_vien

    if tuoi_lon_nhat < tuoi_thanh_vien:
        ban_lon_nhat = thanh_vien[0]
        tuoi_lon_nhat = tuoi_thanh_vien

        print('Tuổi lớn nhất (cho đến thời điểm này) là:     ' +
              str(tuoi_lon_nhat))
        print('Bạn lớn tuổi nhất (cho đến thời điểm này) là: ' + ban_lon_nhat)
        print('')   # In 1 dòng trống

    i = i + 1   # hoặc: i += 1

tuoi_trung_binh = tong_tuoi / so_ban

print('Tuổi trung bình là: ' + str(tuoi_trung_binh))

print('Bạn lớn tuổi nhất là: ' + ban_lon_nhat)

print('=== Kết thúc chương trình ===')
print('')
print('')
