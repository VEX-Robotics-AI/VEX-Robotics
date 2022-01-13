"""
Viết một hàm
- Nhận vào tham số là 1 danh sách các chuỗi
- Trả về chuỗi có độ dài lớn nhất
"""


def find_longest_str(list_of_strs: list[str]) -> str:
    result = None

    for s in list_of_strs:
        if (result is None) or (len(s) > len(result)):
            result = s

    return result


strs = ["90", "name", "*"]

print(f"The longest string is '{find_longest_str(strs)}'.")
