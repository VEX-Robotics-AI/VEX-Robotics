"""
Viết một hàm
- Nhận vào tham số là 1 danh sách các chuỗi
- Trả về chuỗi có độ dài lớn nhất
"""


strs = ["90", "name", "*"]
result = None

for s in strs:
    if (result is None) or (len(s) > len(result)):
        result = s

print(f"The longest string is '{result}'.")
