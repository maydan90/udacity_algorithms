def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    left_boundary = 0
    right_boundary = len(input_list) - 1

    while left_boundary <= right_boundary:
        middle_index = (left_boundary + right_boundary)//2

        if input_list[middle_index] == number:
            return middle_index
        elif input_list[middle_index] < number:
            if input_list[middle_index] > input_list[right_boundary] or input_list[right_boundary] >= number:
                left_boundary = middle_index + 1
            else:
                right_boundary = middle_index - 1
        else:
            if input_list[middle_index] < input_list[left_boundary] or input_list[left_boundary] <= number:
                right_boundary = middle_index - 1
            else:
                left_boundary = middle_index + 1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[2, 1], 1])
test_function([[], 1])
