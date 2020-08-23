def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # trivial cases of empty array or one element array
    if not input_list or len(input_list) == 1:
        return input_list
    zeros_count = 0
    twos_count = 0
    for element in input_list:
        if element == 0:
            zeros_count += 1
        if element == 2:
            twos_count += 1
    ones_count = len(input_list) - zeros_count - twos_count
    return [0 for _ in range(zeros_count)] + [1 for _ in range(ones_count)] + [2 for _ in range(twos_count)]


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
