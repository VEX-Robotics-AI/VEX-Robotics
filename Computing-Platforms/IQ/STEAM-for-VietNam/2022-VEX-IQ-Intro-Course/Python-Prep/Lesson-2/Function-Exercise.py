'''
http://bit.ly/S4V_CS201_Function_Exercise
https://www.robotmesh.com/studio/60bd540c5ba6e20556d7ed10

Dựa vào điểm của các robot,
hãy viết hàm chia các robot trong list về 3 nhóm sau:
     + A: >8-10
     + B: >5-8
     + C: nhỏ hơn bằng 5

Ví dụ:
Input:  [8,4,10,9]
Output: ['B','C','A','A']
'''


# y = f(x)
def phan_loai_robot(danh_sach_diem):
    xep_loai_robot = []

    for diem in danh_sach_diem:
        if diem > 8 and diem <= 10:   # xep loai A
            xep_loai = 'A'
        elif diem > 5 and diem <= 8:   # xep loai B
            xep_loai = 'B'
        elif diem >= 0 and diem <= 5:   # xep loai C
            xep_loai = 'C'
        else:
            xep_loai = 'K'   # khong phu hop
        xep_loai_robot.append(xep_loai)
    return xep_loai_robot


robot_grades = [10, 10, 999, 10]
kq = phan_loai_robot(robot_grades)
# print(kq)

diem_bang_a = [6, 2, 10]
diem_bang_b = [0, 5, 4, 2, 10]
diem_bang_c = [6, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000]

print(phan_loai_robot(diem_bang_a))
print(phan_loai_robot(diem_bang_b))
print(phan_loai_robot(diem_bang_c))
