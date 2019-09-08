def calculator(command, first, second):
    if command == "add":
        return first + second
    elif command == "sub":
        return first - second
    elif command == "multiply":
        return first * second
    elif command == "divide":
        try:
            return first / second
        except ZeroDivisionError:
            #print("Divided by zero.")
            return None
        except TypeError:
            #print("Type error.")
            return None
    else:
        return None

print(calculator("add", 1, 2)) #should print 3
print(calculator("sub", 1, 2)) #should print -1
print(calculator("multiply", 1, 2)) #should print 2
print(calculator("divide", 6, 2)) #should print 3.0
print(calculator("divide", 6, 0)) #divided by zero
print(calculator("divide", 6, "e")) #Type error