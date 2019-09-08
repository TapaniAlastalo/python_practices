commands = [ "add", "sub", "multiply", "divide" ]

def calculator(command, first, second):
    if command == commands[0]:
        return first + second
    elif command == commands[1]:
        return first - second
    elif command == commands[2]:
        return first * second
    elif command == commands[3]:
        try:
            return first / second
        except ZeroDivisionError:
            print("Divided by zero.")
            return None
        except TypeError:
            print("Type error.")
            return None
    else:
        return None

def calculatorProgram():
    choice = 99
    while choice != -1:
        print("0) " + commands[0])
        print("1) " + commands[1])
        print("2) " + commands[2])
        print("3) " + commands[3])
        print("-1) Quit")
        try:
            print("choice: ")
            choice = int(input())
            if choice == -1:
                break;
            print("number: ")
            number1 = float(input())
            print("number: ")
            number2 = float(input())
            print("Result: " + str(calculator(commands[choice], number1, number2)) + "\n")
        except:
            print("Use numbers dummy")

calculatorProgram()