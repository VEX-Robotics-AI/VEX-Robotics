"""
Viết chương trình tính tổng của các số trong một danh sách
"""


def find_sum(list_of_numbers: list[int]) -> int:
    total = 0

    for number in list_of_numbers:
        total += number

    return total


numbers = [1, 2, 7]

print(find_sum(numbers))
