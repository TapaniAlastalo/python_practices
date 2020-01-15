# Translate to chars. Use custom ASCII table (default True)
def translatePointsToWord(points, customASCIITable = True):
    if(customASCIITable == True):
        return LETTERPointsToWord(points)
    else:
        return ASCIIPointsToWord(points)

# Translate to chars. Use custom ASCII table (default True)        
def translateWordToPoints(word, customASCIITable = True):
    if(customASCIITable == True):
        return wordToLETTERPoints(word)
    else:
        return wordToASCIIPoints(word)

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

# HEX <-> INT
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

# ASCII table functions
import ascii_table

# Get letter with index i
def getLETTERByIndex(i):
    return ascii_table.LETTERS[(i%len(ascii_table.LETTERS))]

# Find and the return index of letter c
def findIndexForLETTER(c):
    return ascii_table.LETTERS.index(c)

# Translate characters (word) to LETTER points
def wordToLETTERPoints(word):
    lineSeparator = '\n'
    points = []
    for c in word:
        if(c != lineSeparator):
            points.append(ascii_table.LETTERS.index(c))
    return points

# Translate LETTER points to characters (word)
def LETTERPointsToWord(points):
    word = ""
    for p in points:
        word = word + ascii_table.LETTERS[(p%len(ascii_table.LETTERS))]
    return word