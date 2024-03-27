
DataList = [1, 3, 6,9]

# create an iterator from the list
iterator = iter(DataList)

'''
# get the first element of the iterator
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) # given StopIteration

'''

# iterate through the elements of the iterator
for element in iterator:

    # Print each element
    print(element)

