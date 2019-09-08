def calculator(command, first, second):
    if command == "add":
        return first + second
    elif command == "sub":
        return first - second
    elif command == "multiply":
        return first * second
    else:
        return 0

print(calculator("add", 1, 2)) #should print 3
print(calculator("sub", 1, 2)) #should print -1
print(calculator("multiply", 1, 2)) #should print 2