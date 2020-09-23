import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    pass

# Example Test Case of Ten Integers


values = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(values)

print("Pass" if ((0, 9) == get_min_max(values)) else "Fail")
