#parent class
class animal:
    def speak(self):
        print("Animal is speaking")

class dog(animal):
    def bark(self):
        print("The dog is barking")

class cow(animal):
    def moo(self):
        print("The cow is mooing")

d = dog()
d.speak()

c=cow()
c.moo()
