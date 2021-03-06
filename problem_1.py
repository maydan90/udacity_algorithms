def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if type(number) is not int or number < 0:
        return None

    if number == 0 or number == 1:
        return number

    lower_boundary = 1
    upper_boundary = number
    while upper_boundary - lower_boundary > 1:
        middle = (lower_boundary + upper_boundary)//2
        middle_square = middle * middle
        if middle_square == number:
            return middle
        if middle_square > number:
            upper_boundary = middle
        else:
            lower_boundary = middle
    return lower_boundary


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

print(sqrt(15241578750248846))  # 123456789

print(sqrt(-100))  # None
print(sqrt('1245'))  # None
