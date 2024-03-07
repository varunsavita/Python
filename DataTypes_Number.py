# int: Holds signed intergers of non-limited length.
# Float : Holds floating decimal points and it's accurate upto 15 decimal places.
# Complex : Holds complex numbers.

# Type : Use type() function to know which class of a variable or a value belongs to.

# Type conversion
# Operations like addition and subtraction convert intergers to float implicitly (automatically), if one of the operands is float.

# Built-in-function : int(), Float(), and complex()

data_num = 5
print('value is of type', type(data_num))

data_num = 5.42
print('value is of type', type(data_num))

data_num = 5 + 5j
print('value is of type', type(data_num))

data_num = 5 + 5.2
print('value is of type', type(data_num), 'and value', data_num)

print('value is of type', type(1+ 2.2))

data_num = int(2.3)
print('value is of type', type(data_num))

data_num = int(-3)
print('value is of type', type(data_num), 'and value', data_num)

data_num = float(3)
print('value is of type', type(data_num), 'and value', data_num)

data_num = complex(3)
print('value is of type', type(data_num), 'and value', data_num)

