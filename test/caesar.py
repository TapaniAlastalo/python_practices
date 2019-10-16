import json
import io
import os

letters = [ 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Å', 'Ä', 'Ö'
    ]

#values = []

#def setValues():
#    for letter in letters:
#        values.append(ord(letter.upper()))   

#setValues()

class Message(object):
    def __init__(self, message):
        self.encoded = message

def object_decoder(obj):
    if 'message' in obj: # and obj['__type__'] == 'User':
        return Message(obj['message'])
    return obj

# 65 - 90, 197, 196, 214
def decodeMessage(message, letters, move):
    try:
        length = len(letters)
        move = move % length
        decoded = ""
        for c in message:
            C = c.upper()
            if C == ' ' or C == '.':  #space and dot
                decoded = decoded + C
            else:
                index = letters.index(C)
                newIndex = index + move
                if newIndex < 0:
                    newIndex = length + newIndex
                elif newIndex > length -1:
                    newIndex = newIndex - length

                newC = letters[newIndex]        
                decoded = decoded + newC
    except Exception as e:
        print(e)
        return "bullshit"    
    return decoded

def read_secret_data(fileName):
    secrets = []
    try:
        print(fileName)
        here = os.path.dirname(os.path.abspath(__file__))
        absolutePath = os.path.join(here, fileName)
        #file = open(absolutePath, "r")
        file = io.open(absolutePath, mode="r", encoding="utf-8")
        jsonText = file.read()
        file.close()
        # parse json
        y = json.loads(jsonText)
        messages = y["bullshits"]
        for message in messages:
            #print(message)            
            secrets.append(object_decoder(message))
    except Exception as e:
        print(e)
    return secrets 

#print("letters")
#for letter in letters:
 #   print(letter.upper())
  #print(ord(letter.upper()))

#print("values")
#for value in values:
    #print(value)

def vokaaliCounter(word):
    VOKAALIT = [ 'A', 'E', 'I', 'O', 'U', 'Y', 'Å', 'Ä', 'Ö']
    counter = 0
    for c in word:
        if c in VOKAALIT:
            counter = counter +1
    return counter

def vierasVokaaliFilter(word):
    A_VOKAALIT = [ 'A', 'O', 'U']
    Ä_VOKAALIT = [ 'Ä', 'Ö', 'Y']
    #APU_VOKAALIT = [ 'E', 'I']
    a_vokaalit = False
    ä_vokaalit = False
    for C in word:
        if a_vokaalit == False and C in A_VOKAALIT:
            a_vokaalit = True
        elif ä_vokaalit == False and C in Ä_VOKAALIT:
            ä_vokaalit = True
        elif a_vokaalit == True and ä_vokaalit == True:
            return False
    if a_vokaalit == True and ä_vokaalit == True:
        return False
    else:
        return True


    

def vokaaliFilter(word):
    #return True
    if vierasVokaaliFilter(word):
        vokaalit = vokaaliCounter(word)
        length = len(word)
        vl = float(vokaalit) / float(length) * 100
        # suodata jos vokaalien osuus liian pieni / suuri
        MIN = 30
        MAX = 90
        if vl > MIN and vl < MAX:
            return True
        else:
            return False
    else:
        return False

# Pass if not containing foreign letters
def foreignFilter(word):
    FOREIGNERS = [ 'B', 'C', 'D', 'F', 'Q', 'W', 'X', 'Z', 'Å']
    for C in word:
        if C in FOREIGNERS:
            return False
    return True

# Pass if last letter is vokaali or S, T, N
def lastLetterFilter(word):
    VOKAALIT = [ 'A', 'E', 'I', 'O', 'U', 'Y', 'Ä', 'Ö']
    LAST_LETTERS = ['N', 'T', 'S']
    DOT = '.'
    index = len(word) -1
    C = word[index]
    if C == DOT:        
        word = word[0:len(word) -2]
        C = word[len(word) -1]
    if C in LAST_LETTERS:
        # what is second last?
        C = word[len(word) -2]
        if C in VOKAALIT:
            return True
        else: 
            return False
    elif C in VOKAALIT:
        return True
    return False

def middlePartFilter(word):
    MID_PART_PROBLEMS = ['SSA', 'SSÄ'] 
    for mid_part_problem in MID_PART_PROBLEMS:
        if mid_part_problem in word:
            if word.endswith(mid_part_problem):
                continue
            else:
                #print("Keskellä SSA/SSÄ!!!" + word)
                return False   
    return True

def findExtraErrors(text):
    extraPoints = 0
    E1 = "ILI"
    if E1 in text:
        extraPoints = extraPoints +1
    return extraPoints


def errorFilter(text):    
    ERRORS = [',', ';', '_', ':']
    errorCounter = findExtraErrors(text)
    errorTolerance = 2
    for C in text:
        if C in ERRORS:
            errorCounter = errorCounter +1
    return errorCounter < errorTolerance


def filterBullshit(text):
    words = text.split()  
    bullshit = ""  
    for word in words:
        if foreignFilter(word):
            if lastLetterFilter(word):
                if middlePartFilter(word):
                    if vokaaliFilter(word):
                        bullshit = bullshit + " " + word
                    else:
                        bullshit = bullshit + "_ "
                else:
                    bullshit = bullshit + ": "
            else:
                bullshit = bullshit + "; "
        else:
            bullshit = bullshit + ", "

    if errorFilter(bullshit):
        return True
    else:
        return False




fileName = "secret.txt"
secrets = read_secret_data(fileName)
print("secrets")
for secret in secrets:
    for x in range(1, 30):
        decoded = (decodeMessage(secret.encoded, letters, x))
        #print(decoded)
        if filterBullshit(decoded):
            print(decoded)
    




