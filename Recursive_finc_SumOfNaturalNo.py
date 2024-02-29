# Python program to find the sum of natural using recursive function

def recurFunc_sum(n):
   if n <= 1:
       return n
   else:
       return n + recurFunc_sum(n-1)

# change this value for a different result
num = 10

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recurFunc_sum(num))
