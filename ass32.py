import sys

argList = sys.argv
if len(argList) == 2:
    fileName = argList[1]

    def readFile(fileName):
        try:
            file = open(fileName, "r")
            lines = file.readlines()    # all lines as list
            for line in sorted(lines):
                print(str.strip(line))
            file.close()
        except IOError:
            print("File not found.")
        except:
            print("Something went wrong.")

    readFile(fileName)
else:
    print("Not enough arguments.")