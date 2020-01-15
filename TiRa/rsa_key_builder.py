import random

DEFAULT_P = 229
DEFAULT_Q = 419
DEFAULT_E = 89099
DEFAULT_D = 48443

FAST_P = 17
FAST_Q = 29
FAST_E = 173
FAST_D = 101

# Generate random prime number. Not effective at all.
def generateRandomPrimeNumber(min, max, already_picked = -1):
    r = random.randint(min, max)
    while (isPrime(r) == False or r == already_picked):
        r = random.randint(min, max)
    return r

# Check that number n is prime number
def isPrime(n) :   
    # Corner cases if n <= 3
    if (n <= 1) : 
        return False
    elif (n <= 3) : 
        return True
  
    # Check dividers for 2 and 3 so that we can skip five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    # after first checks i starts from 5
    i = 5
    # i*i must be equal or less than n if i divides n -> n is not prime number
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        # all remaining numbers to be checked can be found 6k ± i
        i = i + 6
  
    return True

# Calculate public key using pre values
def calculatePublicKey(p, q):
    print("calculate public key")
    r = (p-1) * (q-1)
    # random number e between 1 - r
    e = random.randint(1+1, r-1)
    counter = r
    while calculateSYT(e, r) != 1:
        e = random.randint(1+1, r-1)
        # prevent for ever loop
        counter = counter - 1
        if counter == 0:
            return -1
    return e

# Calculate suurin yhteinen tekijä luvuille a ja b
def calculateSYT(a, b):
    print("calculate SYT")
    # ensure that b = bigger
    if a > b:
        c = a
        a = b
        b = c
    base = b
    divider = a
    mod = base % divider 
    while (mod != 0):  
        base = divider      
        divider = mod
        mod = base%divider
    return (divider)

# Calculate secret key using pre values
def calculateSecretKey(p, q, e):
    print("calculate secret key")
    r = (p-1) * (q-1)
    # calculate Eulers phi
    phi = eulerPhi(r)
    # secret key d
    d = (e**(phi-1))%r
    #ed≡1modϕ
    # d != e
    if d == e:
        return -1
    return d

# Calculate euler's phi
# https://stackoverflow.com/questions/18114138/computing-eulers-totient-function by Rodrigo Lopez
def eulerPhi(n):
    phi = int(n > 1 and n)
    for p in range(2, int(n ** .5) + 1):
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p
    #if n is > 1 it means it is prime
    if n > 1: phi -= phi // n 
    return phi