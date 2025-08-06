# Basic Calculator Program

# Step 1: Get inputs
num1 = float(input("Enter the first number:10"))
num2 = float(input("Enter the second number:5"))
operation = input("Enter the operation (+, -, *, /):+")

# Step 2: Perform calculation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation entered.")
