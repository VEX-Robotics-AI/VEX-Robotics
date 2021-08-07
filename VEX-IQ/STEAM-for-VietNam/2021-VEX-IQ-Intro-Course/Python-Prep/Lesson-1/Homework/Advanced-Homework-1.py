"""
Tìm và xuất phần tử có giá trị lớn nhất trong danh sách.
Ví dụ: danh_sach = [1, 5, 2, 3, 13, 2]. Kết quả xuất ra là: 13
"""


numbers = [1, 5, 2, 3, 13, 2]
the_largest_number = None

for number in numbers:
    if (the_largest_number is None) or (number > the_largest_number):
        the_largest_number = number

print(f"The largest number is {the_largest_number}.")
