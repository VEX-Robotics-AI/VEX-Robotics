"""
Viết một hàm
- Nhận vào tham số là 1 danh sách các số nguyên
- Trả về tổng các số lẻ trong danh sách đó
"""


def is_odd(x: int) -> bool:
    return x % 2 != 0


# [125, 259, 59, 90, 80, 70, -90, -70, 33, -33, 55, 90]
numbers = [-60, -70, -67, -77, -55, -111, -1111, -555, -99, 10, 20]

print(sum(
    number  # what to sum
    for number in numbers  # iteration
    if is_odd(number)  # filtering condition
))
