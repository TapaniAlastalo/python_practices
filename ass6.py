def getNumber():
    print("Give number")
    try:
        return int(input())
    except:
        return getNumber()

def compareNumbers(first, second):
    if first >= second:
        return first
    elif second > first:
        return second

print(compareNumbers(getNumber(), getNumber()))

