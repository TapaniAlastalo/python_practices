import math
import random
# Contains used ASCII values
import ascii_table
# File paths
import filepaths

def generateData(k):
    with open(filepaths.TEST_DATA_PATH+ str(k) +filepaths.TXT, 'a') as f:
        multiplier = 1000
        print('Generating %i characters:' % (k * multiplier))
        #Count of used ASCII letters
        count = len(ascii_table.LETTERS)-1
        for y in range(1, k+1):
            print('Iteration %i' % y)
            for x in range(0,multiplier):
                #f.write(chr(random.randint(50,120)))
                f.write(ascii_table.LETTERS[random.randint(0,count)])
        f.write('\n')

# This algorithm generates test data
def generateTestData():
    generateData(1)
    generateData(10)
    generateData(100)
    generateData(1000)
    generateData(10000)

# This algorithm generates test data with constant
def generateTestDataWithConstant(c):
    generateData(c)
    generateData(c)
    generateData(c)
    generateData(c)
    generateData(c)
    
#main()





