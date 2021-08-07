"""
Tìm và xuất phần tử có giá trị lớn nhất trong danh sách.
Ví dụ: danh_sach = [1, 5, 2, 3, 13, 2]. Kết quả xuất ra là: 13.
"""


def find_max(list_of_numbers: list[int]) -> int:
    largest_number = None

    for number in list_of_numbers:
        if (largest_number is None) or (number > largest_number):
            largest_number = number

    return largest_number


def find_min(list_of_numbers: list[int]) -> int:
    smallest_number = None
    for number in list_of_numbers:
        if (smallest_number is None) or (number < smallest_number):
            smallest_number = number

    return smallest_number


numbers = [1, 5, 2, 3, 13, 2]


print(f"The largest number is {find_max(numbers)}.")
print(f"The smallest number is {find_min(numbers)}.")
