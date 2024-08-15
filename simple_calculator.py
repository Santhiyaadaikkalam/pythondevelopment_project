def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    else:
        return num1 / num2

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

while True:
    print("\nCALCULATOR\n")
    calculator()
    select = input("Select operation from 1, 2, 3, 4: ")
    if select in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("TOTAL VALUE:")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if select == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif select == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif select == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif select == '4':
            result = divide(num1, num2)
            if result == "Error! Division by zero.":
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input. Please select a valid operation.")
