list = []
print("Give value for list. (x quits)")
x = input()

# stop if input is x
while x != "x":
    # if found remove from list
    if x in list:
        list.remove(x)
    # else add to list
    else:
        list.append(x)
    x = input()

# print array
print("List:")
for item in list:
    print(item)