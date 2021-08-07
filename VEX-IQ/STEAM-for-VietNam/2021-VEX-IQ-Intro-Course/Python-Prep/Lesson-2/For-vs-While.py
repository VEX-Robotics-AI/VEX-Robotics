"""
http://bit.ly/S4V_CS201_For_While
https://www.robotmesh.com/studio/60bd4cf84271ec49ce231d5e
"""


# Tính tổng các số chẵn nằm trong khoảng từ 1 đến 22

# ===============================================
# Toán tử % (modulo) dùng để chia lấy dư
# print(1%2)
# print(2%2)
# print(3%2)
# print(7%4)

# ===============================================
# for

total = 0
for value in range(1, 23):
    if value % 2 == 0:
        total += value
print('for Loop: ')
print(total)


# ===============================================
# while

total = 0
value = 1
while value < 23:
    if value % 2 == 0:
        total += value
    value += 1
print('while Loop: ')
print(total)


# Có đúng chưa nhỉ?
# --> Tuỳ thuộc yêu cầu đề bài: Có bao gồm cả số 22 không?
