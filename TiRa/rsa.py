import math
import random

# Request shall we try again
def requestAgain():
    print("Again? (y):")
    return input() == "y"

# Request word from user
def requestWord():
    print("Give word:")
    return input()       

# Request word from user
def requestPrimeNumber(prev):
    if prev == 0:
        print("Give prime number:")
    else:
        print("Give second prime number:")
    prime = 0
    try:
        prime = int(input())
        # if not prime request again
        if isPrime(prime) == False:
            print(str(prime) + " is not prime number.")
            prime = requestPrimeNumber(prev)
        if prime == prev:
            print(str(prime) + " is already given.")            
            prime = requestPrimeNumber(prev)
    except:
        prime = requestPrimeNumber(prev)
    return prime

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
            

# Translate characters to ASCII points
def wordToASCIIPoints(word):
    points = []
    for c in word:
        points.append(ord(c))
    return points

# Translate ASCII points to character
def ASCIIPointsToWord(points):
    word = ""
    for p in points:
        print("ASCII pts to word["+ str(p) + " = " + chr(p) +"]")
        word = word + chr(p)
    return word

# RSA coding
def encode(points, k, n):
    encoded = []
    for p in points:
        encoded.append((p**k)%n)
    return encoded

# RSA decoding
def decode(encodedPoints, k, n, d):
    decoded = []
    for p in encodedPoints:
        decoded.append((p**d)%n)
    return decoded

# Calculate public key using pre values
def calculatePublicKey(p, q):
    r = (p-1) * (q-1)
    # random number e between 1 - r
    e = random.randint(1+1, r-1)
    return e

# Calculate secret key using pre values
def calculateSecretKey(p, q, k):
    r = (p-1) * (q-1)
    # calculate Eulers phi
    phi = eulerPhi(r)
    # secret key d
    d = (k**(phi-1))%r
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


# RSA algo
def main():
    # Secret pre values. Could be any prime numbers.
    p = requestPrimeNumber(0) #7
    q = requestPrimeNumber(p) #19
    print("p and q [" + str(p) + "," + str(q) + "]")
    
    # Make public keys
    n = p*q
    e = calculatePublicKey(p, q)
    #e = 5
    print("Public key pair [n, k] for encrypting is [" + str(n) + "," + str(e) + "]")

    # Calculate secret key d
    d = calculateSecretKey(p, q, e)
    print("Secret key d for decrypting is [" + str(d) + "]")

    # Request word from user
    word = requestWord()
    #word = "OIKEIN"
    print("Word : " + word)

    # Translate to points
    points = wordToASCIIPoints(word)
    print("As ASCII points " + str(points))

    # Encode
    encodedPoints = encode(points, e, n)
    # print encoded
    # Translate to chars
    encodedWord = ASCIIPointsToWord(encodedPoints)
    print("Encoded word : " + encodedWord)
    print("As encoded ASCII points " + str(encodedPoints))

    # Decode
    decodedPoints = decode(encodedPoints, e, n, d)
    # print decoded
    print("As decoded ASCII points " + str(decodedPoints))
    # Translate to chars
    decodedWord = ASCIIPointsToWord(decodedPoints)
    print("Decoded word : " + decodedWord)

    # Again?
    if requestAgain() == True:
        main()
    # The end

main()





