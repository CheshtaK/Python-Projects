def add(num1, num2):
    """Returns num1 plus num2"""
    return num1 + num2


def sub(num1, num2):
    """Returns num1 minus num2"""
    return num1 - num2


def mul(num1, num2):
    """Returns num1 times num2"""
    return num1 * num2


def div(num1, num2):
    """Returns num1 divided by num2"""
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Handled division by zero. Returning zero.")
        return 0


def runOperation(operation, num1, num2):
    """Determines the operation to run"""
    if operation == 1 or operation == '+':
        print(add(num1, num2))
    elif operation == 2 or operation == '-':
        print(sub(num1, num2))
    elif operation == 3 or operation == '*':
        print(mul(num1, num2))
    elif operation == 4 or operation == '/':
        print(div(num1, num2))
    else:
        print("I don't understand")


def main():

    validInput = False

    while not validInput:
        try:
            num1 = int(input("Enter first number"))
            num2 = int(input("Enter second number"))
            operation = int(input("What do you want to do? 1.Add, 2.Subtract, 3.Multiply, 4.Divide. Enter number: "))
            validInput = True
        except ValueError:
            print("Invalid input. Try again")
        except:
            print("Unknown error")
        runOperation(operation, num1, num2)
# This is a fancy line of code that will
# only run the main function if we directly execute this
# file. Think of the __name__ variable as an indicator
# assigned by python for the purpose of determining
# if the "main" function should be run. Adding this
# line will enable use to import our calculator
# "module" so we can reuse its functionality.
# If you do not totally understand why this
# works DO NOT WORRY. Just know what it does
# and WHY we are using it.
if __name__ == "__main__":
    main()
