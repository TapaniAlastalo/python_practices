import math
import time
# Contains used ASCII methods
import ascii_translator
# File paths
import filepaths

# RSA coding
def encode(points, e, n):
    encoded = []
    for m in points:
        encoded.append((m**e)%n)
    return encoded

# RSA encrypt algo
# This algorithm reads in test data from file, encrypts it, and times the process
def encrypt(n, e, line, counter, runTime, flags = 1):     
    # Translate to points
    points = ascii_translator.translateWordToPoints(line, True)
    #Set timer
    start_time = time.process_time()
    # Encode
    encodedPoints = encode(points, e, n)
    # Stop timer
    duration = time.process_time() - start_time
    # Save to file
    saveToFile(encodedPoints, duration, counter, runTime, flags)
    return encodedPoints
    

def saveToFile(encodedPoints, duration, counter, runTime, flags = 1):
    if flags != -1:
        #Save results
        print('Encryption duration: %s seconds' % str(duration))
        with open(filepaths.ENC_RESULTS_PATH+str(counter) + '_' + str(runTime) +filepaths.CSV, 'a') as r:
            r.write('%s\n' % str(duration))    
        if flags > 2 or flags == 0:      
            # Translate to chars          
            encodedWord = ascii_translator.translatePointsToWord(encodedPoints, True)
            # Save texts # FOR TEST PURPOSES
            with open(filepaths.ENC_TEXT_PATH+str(counter) + '_' + str(runTime) +filepaths.TXT, 'a') as t:
                t.write(encodedWord)   #t.write('%s\n' % encodedWord)
            if flags > 3 or flags == 0:
                # Save points
                with open(filepaths.ENC_POINTS_PATH+str(counter) + '_' + str(runTime) +filepaths.TXT, 'a') as t:
                    t.write('%s\n' % encodedPoints)
        






