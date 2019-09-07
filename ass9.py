#example lists:
list1 = [1,2,3,4,5] #the function should return 5
list2 = [1,3,4,2]   #the function should return 4

def largest(list):
    largest = list[0]
    for n in list:
        if n > largest:
            largest = n
    return largest

print(largest(list1))
print(largest(list2))