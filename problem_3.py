from collections import defaultdict


def number_frequency(arr):
    frequencies = defaultdict(int)
    for number in arr:
        frequencies[number] += 1
    return frequencies


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    frequencies = number_frequency(input_list)
    first_number, second_number = '', ''

    for digit in range(9, -1, -1):
        if digit in frequencies:
            frequency = frequencies[digit]
            frequency_split = frequency//2
            common_add = str(digit)*frequency_split
            first_number += common_add
            second_number += common_add
            if frequency % 2 == 1:
                if len(first_number) > len(second_number):
                    second_number += str(digit)
                else:
                    first_number += str(digit)

    if first_number == '':
        first_number = '0'
    if second_number == '':
        second_number = '0'
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

test_function([[7, 7, 7, 9, 8], [987, 77]])

test_function([[1]*21, [11111111111, 1111111111]])

test_function([[], [0, 0]])
test_function([[7], [0, 7]])
