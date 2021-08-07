"""
Đếm số phần tử có cùng giá trị lớn nhất trong danh sách.
Ví dụ: danh_sach = [1, 5, 2, 2, 9, 1, 4, 9, 2, 9, 2]
Kết quả xuất ra là: Có 3 phần tử có giá trị là 9
"""


numbers = [1, 5, 2, 2, 9, 1, 4, 9, 2, 9, 2]

# Find the largest number
the_largest_number = None
for number in numbers:
    if (the_largest_number is None) or (number > the_largest_number):
        the_largest_number = number

# Find the count of the largest number
count = 0
for number in numbers:
    if number == the_largest_number:
        count += 1


print(f"Có {count} phần tử có giá trị là {the_largest_number}.")
