x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

operation = input("Which mathematical operation you want (+, -, *, /): ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("Error")
