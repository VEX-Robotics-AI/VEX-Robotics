"""
Đếm số phần tử có cùng giá trị lớn nhất trong danh sách.
Ví dụ: danh_sach = [1, 5, 2, 2, 9, 1, 4, 9, 2, 9, 2]
Kết quả xuất ra là: Có 3 phần tử có giá trị là 9
"""


def find_max(list_of_numbers: list[int]) -> int:
    largest_number = None

    for number in list_of_numbers:
        if (largest_number is None) or (number > largest_number):
            largest_number = number

    return largest_number


def find_count_of_number_in_list(
        number_to_count: int,
        list_of_numbers: list[int]) -> int:
    count = 0

    for number in list_of_numbers:
        if number == number_to_count:
            count += 1

    return count


numbers = [1, 5, 2, 2, 9, 1, 4, 9, 2, 9, 2]

the_largest_number = find_max(numbers)

print(f"Có {find_count_of_number_in_list(the_largest_number, numbers)} "
      f"phần tử có giá trị là {the_largest_number}.")
