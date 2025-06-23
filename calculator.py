def calc_operations():
    print("\n===== Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def main():
    while True:
        calc_operations()
        choice = input("Enter Choice (1-5): ")

        if choice == '5':
            print("Exiting Calculator...")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Please Enter Valid Choice.")
            continue

        try:
            num1 = float(input("Enter number 1: "))
            num2 = float(input("Enter number 2: "))
        except ValueError:
            print("Please enter numeric values only.")
            continue

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)

        print("\nResult: ", result)


if __name__ == "__main__":
    main()
