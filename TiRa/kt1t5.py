def Fi(k):
    if k == 1:
        return 1
    elif k == 0:
        return 1
    else: 
        return Fi(k-1) + Fi(k-2)

def iFi(k):
    n = 0
    prev = 0
    prevprev = 0
    while n < k:
        if n == 0:
            prev = 1
        elif n == 1:
            prevprev = prev
        else:
            now = prevprev + prev
            prevprev = prev
            prev = now
        n = n +1
    return prevprev + prev

def requestNumber():
    print("Give number")
    try:
        number = int(input())        
        print(iFi(number))
    except:
            print("Problem!")
            requestNumber()


requestNumber()





