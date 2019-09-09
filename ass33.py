class Dog:
    def __init__(self, name, sound, walking_speed, running_speed): #The initializer that takes a member variables
        self.name = name
        self.sound = sound
        self.walking_speed = walking_speed
        self.running_speed = running_speed
    
    def walk(self):  #prints a walking speed
        print("Walks " + str(self.walking_speed) + " km/h")
    
    def run(self): #prints a running speed
        print("Runs " + str(self.running_speed) + " km/h")
    
    def bark(self): #prints a barking sound
        print("Says: " + self.sound)
    
    def print_name(self): #prints dog's name
        print("Name is " + self.name)

dog1 = Dog("Jeppe", "Wuf Wuf", 3, 14)
dog1.print_name()
dog1.bark()
dog1.walk()
dog1.run()

dog2 = Dog("Gubbe", "Hauhau", 1, 3)
dog2.print_name()
dog2.bark()
dog2.walk()
dog2.run()
