import math

# Request word from user
def requestWord():
    print("Give word:")
    return input()        

# Request word from user
def requestPrimeNumber():
    print("Give prime number:")
    prime = 0
    try:
        prime = int(input())        
    except:
        prime = requestPrimeNumber()
    return prime
            

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
    for e in encodedPoints:
        decoded.append((e**d)%n)
    return decoded

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


# RSA algo opened
def main():
    # Request word from user
    word = requestWord()
    #word = "OIKEIN"
    print("Word : " + word)

    # Translate to points
    points = wordToASCIIPoints(word)
    print("As ASCII points " + str(points))

    # RSA coding
    # Secret pre values. Could be any prime numbers.
    p = requestPrimeNumber() #7
    q = requestPrimeNumber() #19
    print("p and q [" + str(p) + "," + str(q) + "]")
    # Make public keys
    n = p*q
    k = 5
    print("public key pair is [" + str(n) + "," + str(k) + "]")

    # Encode
    encodedPoints = encode(points, k, n)
    # print encoded
    # Translate to chars
    encodedWord = ASCIIPointsToWord(encodedPoints)
    print("Encoded word : " + encodedWord)
    print("As encoded ASCII points " + str(encodedPoints))

    # Decode
    d = calculateSecretKey(p, q, k)
    decodedPoints = decode(encodedPoints, k, n, d)
    # print decoded
    print("As decoded ASCII points " + str(decodedPoints))
    # Translate to chars
    decodedWord = ASCIIPointsToWord(decodedPoints)
    print("Decoded word : " + decodedWord)

    # The end

main()





