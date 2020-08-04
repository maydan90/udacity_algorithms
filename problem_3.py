def merge(arr1, arr2):
    idx1, idx2 = 0, 0
    output = []

    while idx1 < len(arr1) and idx2 < len(arr2):
        if arr1[idx1] >= arr2[idx2]:
            output.append(arr1[idx1])
            idx1 += 1
        else:
            output.append(arr2[idx2])
            idx2 += 1

    output.extend(arr1[idx1:])
    output.extend(arr2[idx2:])
    return output


def reversed_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle_index = len(arr) // 2
    return merge(reversed_merge_sort(arr[:middle_index]), reversed_merge_sort(arr[middle_index:]))


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_list = reversed_merge_sort(input_list)
    first_number, second_number = '', ''
    for idx, element in enumerate(sorted_list):
        if idx % 2 == 0:
            first_number += str(element)
        else:
            second_number += str(element)
    return int(first_number), int(second_number)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
