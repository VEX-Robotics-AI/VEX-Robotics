"""
Viết chương trình kiểm tra với 2 số nguyên a và b,
a có chia hết cho b hay không
"""


def is_divisible_by(x: int, y: int) -> bool:
    return x % y == 0


a = 109
b = 10

print(is_divisible_by(x=a, y=b))
