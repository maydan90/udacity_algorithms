import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return None, None

    min_value = ints[0]
    max_value = ints[0]

    for number in ints:
        if number < min_value:
            min_value = number
        elif number > max_value:
            max_value = number
    return min_value, max_value

# Example Test Case of Ten Integers


values = [i for i in range(0, 1000)]  # a list containing 0 - 9
random.shuffle(values)

print("Pass" if ((0, 999) == get_min_max(values)) else "Fail")
