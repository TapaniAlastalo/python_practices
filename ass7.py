def getNumber():
    print("Give number")
    try:
        return int(input())
    except:
        return getNumber()

def checkNumbers(first, second):
    if (first + second) % 2 == 0:
        print("Yes it is!")
    else:
        print("Nope")

checkNumbers(getNumber(), getNumber())