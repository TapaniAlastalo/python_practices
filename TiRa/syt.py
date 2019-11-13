# Calculate suurin yhteinen tekijä luvuille a ja b
def calculateSYT(a, b):
    # ensure that b = bigger
    if a > b:
        c = a
        a = b
        b = c
    base = b
    divider = a
    mod = base % divider 
    while (mod != 0):# and mod != 1):  
        base = divider      
        divider = mod
        mod = base%divider
        print("base:" + str(base))
        print("divider:" + str(divider))
        print("modulus:" + str(mod))

    comp1 = a / divider
    comp2 = b / divider
    #print("Compare1: " + str(comp1))
    #print("Compare2: " + str(comp2))
    #print("Compare1/Compare2: " + str(comp1/comp2))
    #print("Compare2/Compare1: " + str(comp2/comp1))
    #print("a/Compare2: " + str(a/comp2))
    #print("b/Compare1: " + str(b/comp1))

    return (divider)

print("SYT calculator..")
a = 1020
b = 6076
x = calculateSYT(a,b)
print("SYT [" + str(a) + ", " + str(b) + "] = " + str(x))
print("SYT calculator..")
a = 2740
b = 1760
x = calculateSYT(a,b)
print("SYT [" + str(a) + ", " + str(b) + "] = " + str(x))
print("SYT calculator..")
a = 30
b = 50
x = calculateSYT(a,b)
print("SYT [" + str(a) + ", " + str(b) + "] = " + str(x))
print("SYT calculator..")
a = 1027
b = 1508
x = calculateSYT(a,b)
print("SYT [" + str(a) + ", " + str(b) + "] = " + str(x))