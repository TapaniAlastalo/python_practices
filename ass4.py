persons = ["alice", "bob", "craig", "dave", "elisabeth", "frank", "george"]  
i = 0
for person in persons:
    if i % 2 == 0:
        print (str(i) + ":" + person)
    i += 1