import math
import random

LETTERS = [ 'A', 'B', 'C', 'D', 'E', 'F', 
            'G', 'H', 'I', 'J', 'K', 'L', 
            'M', 'N', 'O', 'P', 'Q', 'R', 
            'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', 'Å', 'Ä', 'Ö',
            'a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'å', 'ä', 'ö',
            ' ', '-', ',', '.', '_', ':', ';'  ]

# Find letter and return index of that letter
def findLetterIndex(c):
    return LETTERS.index(c)

# Request shall we try again
def requestAgain():
    print("Again? (y):")
    return input() == "y"

# Request word from user
def requestWord():
    print("Give word:")
    word = ""
    try:
        word = input()

    except:
        word = requestWord()
    return word       

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
        #print("ASCII pts to word["+ str(p) + " = " + chr(p) +"]")
        word = word + chr(p)
    return word

# Translate characters to LETTER points
def wordToLETTERPoints(word):
    points = []
    for c in word:
        points.append(LETTERS.index(c))
    return points

# Translate LETTER points to character
def LETTERPointsToWord(points):
    word = ""
    for p in points:
        #point = p%(len(LETTERS))
        #print("LETTER pts to word["+ str(p) + " = " + str(LETTERS[(p%len(LETTERS))]) +"]")
        word = word + LETTERS[(p%len(LETTERS))]
    return word


# RSA coding
def encode(points, e, n):
    encoded = []
    for m in points:
        encoded.append((m**e)%n)
    return encoded

# RSA decoding
def decode(encodedPoints, d, n):
    decoded = []
    for x in encodedPoints:
        decoded.append((x**d)%n)
    return decoded

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

# Calculate euler's phi
# https://stackoverflow.com/questions/18114138/computing-eulers-totient-function by Rodrigo Lopez
def eulerPhi(n):
    print("calculate euler phi")
    phi = int(n > 1 and n)
    for p in range(2, int(n ** .5) + 1):
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p
    #if n is > 1 it means it is prime
    if n > 1: 
        phi -= phi // n 
    return phi

# alter Ints to hexes
def intsToHexes(ints):
    hexes = []
    for i in ints:
        hexes.append(hex(i))
    return hexes

# alter hexes to Ints
def hexesToInts(hexes):
    points = []
    for hx in hexes:
        points.append(int(hx, 16))
    return points


# RSA algo
def main():
    try:
        # Secret pre values. Could be any prime numbers.
        p = requestPrimeNumber(0) #7
        q = requestPrimeNumber(p) #19
        print("p and q [" + str(p) + "," + str(q) + "]")
        
        # Make public keys
        n = p*q
        e = calculatePublicKey(p, q)
        # no e found
        if e == -1:
            raise ValueError('No public key e couldn\'t be determinated')
        #e = 5
        print("Public key pair [n, e] for encrypting is [" + str(n) + "," + str(e) + "]")

        # Calculate secret key d
        d = calculateSecretKey(p, q, e)
        # no e found
        if d == -1:
            raise ValueError('No secret key d couldn\'t be determinated')
        print("Secret key d for decrypting is [" + str(d) + "]")

        # Request word from user
        word = requestWord()
        #word = "OIKEIN"
        print("Word : " + word)

        # Translate to points
        # points = wordToASCIIPoints(word)
        # print("As ASCII points " + str(points))
        points = wordToLETTERPoints(word)
        print("As LETTER points " + str(points))

        # Encode
        encodedPoints = encode(points, e, n)
        # print encoded
        # Translate to chars
        encodedWord = LETTERPointsToWord(encodedPoints)
        print("As encoded LETTER points " + str(encodedPoints))
        print("Encoded word : " + encodedWord)
        # HEX
        hx = intsToHexes(encodedPoints)
        print("As encoded HEX " + str(hx))
        #dx = hexesToInts(hx)
        #print("As encoded Int " + str(dx))
        
        # Decode
        decodedPoints = decode(encodedPoints, d, n)
        print("As decoded points " + str(decodedPoints))
        # HEX
        hx = intsToHexes(decodedPoints)
        print("As decoded HEX " + str(hx))
        # Translate to chars
        # decodedWord = ASCIIPointsToWord(decodedPoints)
        decodedWord = LETTERPointsToWord(decodedPoints)
        print("Decoded word : " + decodedWord)
    except ValueError as error:
        print(error.args)
    

    # Again?
    if requestAgain() == True:
        main()
    # The end

main()





