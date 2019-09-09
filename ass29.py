import sys

def readFile(fileName):
    try:
        file = open(fileName, "r")
        #line = file.read() # all as they are on file
        #line = file.readline() # one line
        lines = file.readlines()    # all lines as list
        for line in sorted(lines):
            print(str.strip(line))
        file.close()
    except:
        print("Something went wrong")

readFile("example_file.txt")
