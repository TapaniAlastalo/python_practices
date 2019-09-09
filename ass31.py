import sys

def readFile(fileName):
    try:
        file = open(fileName, "r")
        lines = file.readlines()    # all lines as list
        for line in sorted(lines):
            print(str.strip(line))
        file.close()
    except:
        print("Something went wrong")

def writeToFile(fileName, line):
    try:
        file = open(fileName, "a")  # append, w = overwrite
        file.write("\n" + line) # write one line, with a newline!
        file.close()
        print(line + " wrote to file " + fileName)
    except:
        print("Something went wrong")

commands = [ "read", "write", "delete" ]
fileName = "example_file.txt"

def deleteFromFile(fileName, line):
    try:
        # open for read and search
        file = open(fileName, "r")  # read
        lines = file.readlines()    # all lines as list
        if line in lines:
            lines.remove(line)
        elif (line + "\n") in lines:
            lines.remove(line +"\n")
        file.close()

        # overwrite with new list
        file = open(fileName, "w")  # overwrite
        file.writelines(lines) # write lines
        file.close()
        print(line + " deleted from file " + fileName)
    except:
        print("Something went wrong")

commands = [ "read", "write", "delete" ]
fileName = "example_file.txt"


def myJournal():
    choice = 99
    while choice != -1:
        print("\n0) " + commands[0])
        print("1) " + commands[1])
        print("2) " + commands[2])
        print("-1) Quit")
        try:
            print("choice: ")
            choice = int(input())
            if choice == -1:    # quit
                break
            elif choice == 0:
                readFile(fileName)
            elif choice == 1:
                sys.stdout.write("Write to file: ")
                text = input()
                writeToFile(fileName, text)
            elif choice == 2:
                readFile(fileName)
                sys.stdout.write("Delete from file: ")
                text = input()
                deleteFromFile(fileName, text)
        except:
            print("Use numbers dummy")

myJournal()