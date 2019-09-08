def division(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        print("Divided by zero")
        return 0
    except:
        return 0

print(division(2, 0))   # divided by zero
print(division(6, 2))   # 3.0