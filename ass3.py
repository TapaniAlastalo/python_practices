a = ""
for x in range(0, 10):
    a += "aa"
    b = ""
    for y in range(0, 10-x):
        b += " "
    print(b + a)