def recursive_func(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * recursive_func(x-1))


num = 5
print("The factorial of", num, "is", recursive_func(num))