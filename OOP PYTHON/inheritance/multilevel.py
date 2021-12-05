
class Animal(object):
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print("%s is eating %s" %(self.name, food))

class Dog(Animal):
    def fetch(self,thing):
        print("%s is fetching %s" %(self.name,thing))

class Cat(Animal):
    def swatstring(self):
        print("%s is swat the string" %(self.name))

d=Dog("kallu")
d.eat("Roti")
d.fetch("Haddi")


c=Cat("Billu")
c.eat("Fish")
c.swatstring()

#d.swatstring()
