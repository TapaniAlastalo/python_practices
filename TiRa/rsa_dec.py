import math
import time
# Contains used ASCII methods
import ascii_translator
# File paths
import filepaths
# Regex
import re

# RSA decoding
def decode(encodedPoints, d, n):
    decoded = []
    for x in encodedPoints:
        decoded.append((x**d)%n)
    return decoded

# Split string of numbers to Int array
def splitToIntArray(line):
    line = line[1:-2]
    line = re.sub(',', "", line)

    array = []
    for x in line.split():
        array.append(int(x))
    return array

# RSA decrypt algo.
def decrypt(n, d, encodedPoints, counter, runTime, flags = 1):
    # split line to int array
    #encodedPoints = splitToIntArray(line)
    # Start timer
    start_time = time.process_time()                
    decodedPoints = decode(encodedPoints, d, n)
    #Stop timer
    duration = time.process_time() - start_time
    # Save to file
    saveToFile(decodedPoints, duration, counter, runTime, flags)
    

def saveToFile(decodedPoints, duration, counter, runTime, flags = 1):
    if flags != -1:
        #Save results to file
        print('Decryption duration: %s seconds' % str(duration))
        with open(filepaths.DEC_RESULTS_PATH+ str(counter) + '_' + str(runTime) +filepaths.CSV, 'a') as t:
            t.write('%s\n' % str(duration))
        if flags > 2 or flags == 0:       
            # Translate to points                  
            decodedWord = ascii_translator.translatePointsToWord(decodedPoints, True)
            # Save texts
            with open(filepaths.DEC_TEXT_PATH+ str(counter) + '_' + str(runTime) +filepaths.TXT, 'a') as t:
                t.write(decodedWord)   #t.write('%s\n' % decodedWord)
            if flags > 3 or flags == 0:
                # Save points
                with open(filepaths.DEC_POINTS_PATH+ str(counter) + '_' + str(runTime) +filepaths.TXT, 'a') as t:
                    t.write('%s\n' % decodedPoints)



        

        





