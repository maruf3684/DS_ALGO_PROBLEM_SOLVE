
class Animal(object):
    def __init__(self,breed):
        self.breed =breed

class Dog(Animal):
    def __init__(self,name,breed):
        #super().__init__(breed) or 
        super(Dog,self).__init__(breed)
        self.name = name

puppy=Dog("Puppy","Bulldog")
print(puppy.name,puppy.breed)
tuppy=Dog("tuppy","Bulldog")
print(tuppy.name,tuppy.breed)
