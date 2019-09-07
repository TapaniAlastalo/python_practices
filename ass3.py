
for x in range(0, 11):
    a = ""
    b = ""
    for y in range(0, 10-x):
        b += " "
    for y in range(0, x):
        a += "aa"
    print(b + a)