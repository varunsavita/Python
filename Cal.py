# Program make a simple calculator
class cal:
    # This function adds two numbers
    def add(x, y):
        return x + y

    # This function subtracts two numbers
    def subtract(x, y):
        return x - y

    # This function multiplies two numbers
    def multiply(x, y):
        return x * y

    # This function divides two numbers
    def divide(x, y):
        return x / y

    # This function modulus two numbers
    def modulus(x, y):
        return x % y

    def binary(x):
        return ("{0:b}".format(int(x)))

    def octal(x):
        return ("{0:o}".format(int(x)))

    def hexa(x):
        return ("{0:x}".format(int(x)))


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulus")
print("6.Floor Division")
print("7.Power")
print("8.Binary, Octal, Hexa format")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7/8): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
        if choice == '6':
            while True:
                num1 = int(input("Enter number: "))
                if num1 >= 0:
                    break
                else:
                    print("Enter Positive number")
        elif choice in ('1', '2', '3', '4', '5'):
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", cal.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", cal.subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", cal.multiply(num1, num2))

        elif choice == '4':
            try:
                result = cal.divide(num1, num2)
                print(result)
            except Exception as e:
                print(e)
            # print(num1, "/", num2, "=", cal.divide(num1, num2))

        elif choice == '5':
            print(num1, "%", num2, "=", cal.modulus(num1, num2))
        elif choice == '6':
            print("binary", "=", cal.binary(num1))
            print("octal", "=", cal.octal(num1))
            print("hexa", "=", cal.hexa(num1))


        # check if user wants another calculation
        # break the while loop if answer is no
        while True:
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation.lower() == "yes":
                break
            else:
                print("Please enter valid input")
        if next_calculation.lower() == "no":
            break

    else:
        print("Invalid Input")
