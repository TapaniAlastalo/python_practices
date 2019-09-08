def division(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        print("Divided by zero")
    except TypeError:
        print("One or both of your parameters are wrong type!")
    except:
        print("Something went wrong.")

print(division(2, 0))   # divided by zero
print(division(6, 2))   # 3.0
print(division("hei", 2)) # Type error