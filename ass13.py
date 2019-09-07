def dog_sleeps(name, time): #prints: X sleeps Y hours
    print(name + " sleeps " + str(time) + " hours")
def dog_walks(name, speed): #prints: X walks Y speed
    print(name + " walks " + str(speed) + " km/h speed")
def dog_runs(name, speed):  #prints: X runs Y speed
    print(name + " runs " + str(speed) + " km/h speed")
def dog_barks(name, sound): #prints: X barks with a sound Y
    print(name + " barks with a sound " + sound)

#For example:
name = "Musti"
dog_sleeps(name, 5)
dog_walks(name, 10) #Musti walks 10.00km/h speed
dog_runs(name, 35) 
dog_barks(name,"wuf wuf") # Musti barks with a sound "wuf wuf"