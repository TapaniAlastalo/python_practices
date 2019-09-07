#example lists:
list1 = [1,2,3,4,5] #the function should return 15
list2 = [1,1,1,1]   #the function should return 4

def sum1(list):
    sum = 0
    for n in list:
        sum += n
    return sum

print(sum1(list1))
print(sum1(list2))