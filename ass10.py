def reverse(list):
    reverse = []
    while len(list):
        reverse.append(list.pop())
    return reverse

print(reverse([1,2,3,4])) #prints [4,3,2,1]
print(reverse(["aa", "bb", "cc"])) #prints ["cc", "bb", "aa"]