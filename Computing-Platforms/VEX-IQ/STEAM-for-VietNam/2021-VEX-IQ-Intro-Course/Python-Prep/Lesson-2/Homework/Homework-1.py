"""
Tính trung bình cộng các số lẻ từ 1 đến 50
"""


def is_odd(x: int) -> bool:
    return x % 2 != 0


def is_even(x: int) -> bool:
    return x % 2 == 0


def average_odds_by_while_loop(up_to_number: int) -> int:
    i = 0
    total_of_odds = 0
    n_odds = 0
    while i < up_to_number:
        i += 1
        if is_odd(i):
            total_of_odds += i
            n_odds += 1

    return total_of_odds / n_odds


def average_odds_by_for_loop(up_to_number: int) -> int:
    total_of_odds = 0
    n_odds = 0
    for i in range(1, up_to_number + 1):
        if is_odd(i):
            total_of_odds += i
            n_odds += 1

    return total_of_odds / n_odds


def advanced_average_odds(up_to_number: int) -> int:
    total_of_odds = sum(i   # what to sum
                        for i in range(1, up_to_number + 1)   # iteration
                        if is_odd(i)   # filtering condition
                        )

    n_odds = sum(1  # what to sum
                 for i in range(1, up_to_number + 1)  # iteration
                 if is_odd(i)  # filtering condition
                 )

    return total_of_odds / n_odds


def average_evens_by_while_loop(up_to_number: int) -> int:
    i = 0
    total_of_evens = 0
    n_evens = 0
    while i < up_to_number:
        i += 1
        if is_even(i):
            total_of_evens += i
            n_evens += 1

    return total_of_evens / n_evens


def average_evens_by_for_loop(up_to_number: int) -> int:
    total_of_evens = 0
    n_evens = 0
    for i in range(1, up_to_number + 1):
        if is_even(i):
            total_of_evens += i
            n_evens += 1

    return total_of_evens / n_evens


def advanced_average_evens(up_to_number: int) -> int:
    total_of_evens = sum(i   # what to sum
                         for i in range(1, up_to_number + 1)   # iteration
                         if is_even(i)   # filtering condition
                         )

    n_evens = sum(1   # what to sum
                  for i in range(1, up_to_number + 1)  # iteration
                  if is_even(i)  # filtering condition
                  )

    return total_of_evens / n_evens


UP_TO_NUMBER = 50

print("The average of the evens up to "
      f"{UP_TO_NUMBER} is {average_evens_by_for_loop(UP_TO_NUMBER)}")
print("The average of the evens up to "
      f"{UP_TO_NUMBER} is {average_evens_by_while_loop(UP_TO_NUMBER)}")
print("The average of the evens up to "
      f"{UP_TO_NUMBER} is {advanced_average_evens(UP_TO_NUMBER)}")

print("The average of the odds up to "
      f"{UP_TO_NUMBER} is {average_odds_by_for_loop(UP_TO_NUMBER)}")
print("The average of the odds up to "
      f"{UP_TO_NUMBER} is {average_odds_by_while_loop(UP_TO_NUMBER)}")
print("The average of the odds up to "
      f"{UP_TO_NUMBER} is {advanced_average_odds(UP_TO_NUMBER)}")
