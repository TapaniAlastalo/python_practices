def sum2(n):
    sum = 0
    for x in range(0, n + 1):
        sum += x
    return sum

print(sum2(3)) #prints: 6
print(sum2(12)) #prints: 78