def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # trivial cases of empty array or one element array
    if not input_list or len(input_list) == 1:
        return input_list

    last_zero_idx = 0
    first_two_idx = len(input_list) - 1
    current_idx = 0

    while current_idx <= first_two_idx:
        if input_list[current_idx] == 0:
            input_list[current_idx], input_list[last_zero_idx] = input_list[last_zero_idx], 0
            last_zero_idx += 1
            current_idx += 1
        elif input_list[current_idx] == 2:
            input_list[current_idx], input_list[first_two_idx] = input_list[first_two_idx], 2
            first_two_idx -= 1
        else:
            current_idx += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([])
test_function([0])
test_function([1])
test_function([2])

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

test_function([2 for _ in range(1000)] + [1 for _ in range(1000)] + [0 for _ in range(1000)])
