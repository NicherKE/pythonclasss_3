class person:
    def __init__(self,name, age, gender):
        self.name =name
        self.age =age
        self.gender = gender

def details(self):
    print(self.name, "is studying")

p=person("Nicher",21, "male")
p.details()