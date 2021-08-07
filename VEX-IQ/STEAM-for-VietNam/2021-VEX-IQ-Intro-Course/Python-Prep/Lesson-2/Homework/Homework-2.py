"""
Viết một hàm
- Nhận vào tham số là 1 danh sách các số nguyên
- Trả về tổng các số lẻ trong danh sách đó
"""


def is_odd(x: int) -> bool:
    return x % 2 != 0


numbers = [-67]  # [125, 259, 59, 90, 80, 70, -90, -70, 33, -33, 55, 90]
result = 0

for number in numbers:
    if is_odd(number):
        result += number

print(result)
