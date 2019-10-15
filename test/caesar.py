import json
import sys

def read_secret_data(fileName):
    secrets = []
    try:
        print(fileName)
        file = open(fileName, "r")
        lines = file.readlines()    # all lines as list
        file.close()
        
        print("pullu")
        jsonText = ""
        for line in lines:
            jsonText += line
        
        # parse json
        print(jsonText)
        y = json.loads(jsonText)
        print(str(y))
    except:
        print("Something went wrong")
    return secrets 


fileName = "secret.txt"
secrets = read_secret_data(fileName)




