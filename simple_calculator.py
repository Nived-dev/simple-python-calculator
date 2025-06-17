'''Simple calculator(Python CLI Project'''

def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def modulus(x,y):
    return x % y

def power(x,y):
    return x ** y

while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Exit")

    choice = input("Choose an operation (1/2/3/4/5/6/7):")

    if choice == "7":
        print("Exiting calculator. Goodbye!")
        break

    if choice in ("1", "2", "3", "4", "5", "6"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("please enter valid number!")
            continue

        if choice == "1":
            print(f"Result: {add(num1,num2)}")
        elif choice == "2":
            print(f"Result: {substract(num1,num2)}")
        elif choice == "3":
            print(f"Result: {multiply(num1,num2)}")
        elif choice == "4":
            print(f"Result: {divide(num1,num2)}")
        elif choice == "5":
            print(f"Result: {modulus(num1,num2)}")
        elif choice == "6":
            print(f"Result: {power(num1,num2)}")
    else:
        print("Invalid choice, please select from 1 to 7.")
