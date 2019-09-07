vows = [ "a", "e", "o", "u", "y" ]

def vowels(text):
    count = 0
    for x in text:
        if x in vows:
            count += 1
    return count

print(vowels("aaa")) # prints: 3
print(vowels("aba")) # prints: 2
print(vowels("bca")) # prints: 1