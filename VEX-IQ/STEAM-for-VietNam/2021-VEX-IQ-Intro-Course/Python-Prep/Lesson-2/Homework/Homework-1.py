"""
Tính trung bình cộng các số lẻ từ 1 đến 50
"""


i = 0
total_of_odds = 0
n_odds = 0
while i < 50:
    i += 1
    if i % 2 != 0:
        total_of_odds += i
        n_odds += 1

print(total_of_odds / n_odds)
