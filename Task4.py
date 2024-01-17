def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def reminder(x, y):
    return x % y

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /, %): ")

# Call the function based on the operator and print the result
if operator == "+":
    print("The result is: ", add(num1, num2))
elif operator == "-":
    print("The result is: ", subtract(num1, num2))
elif operator == "*":
    print("The result is: ", multiply(num1, num2))
elif operator == "/":
    print("The result is: ", divide(num1, num2))
elif operator == "%":
    print("The result is: ", reminder(num1, num2))
else:
    print("Invalid operator.")