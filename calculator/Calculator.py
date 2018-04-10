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
    if operation == 1:
        print(add(num1, num2))
    elif operation == 2:
        print(sub(num1, num2))
    elif operation == 3:
        print(mul(num1, num2))
    elif operation == 4:
        print(div(num1, num2))
    else:
        print("I don't understand")


def main():

    userContinue = True
    while userContinue:
        validInput = False

        while not validInput:
            try:
                num1 = int(input("Enter first number"))
                num2 = int(input("Enter second number"))
                operation = int(input("What do you want to do? 1.Add, 2.Subtract, 3.Multiply, 4.Divide. "
                                      "Enter number: "))
                validInput = True
            except ValueError:
                print("Invalid input. Try again")
            except:
                print("Unknown error")

        runOperation(operation, num1, num2)

        userYN = input("Would you like to run another calculation? ('y' for yes or any other value to exit)")
        if(userYN != 'y'):
            userContinue = False
            break
        else:
            continue


main()