
#!make custom stack class using deque

from collections import deque

class Stack(object):
    def __init__(self):
        self.container = deque()   #deque class er object banalam / nam delam container

    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def size(self):
        return len(self.container) 
    def is_empty(self):
        return len(self.container) == 0
    def read(self):
        return self.container[-1]
    def print(self):
        for i in self.container:
         print(i,end=" ")
        print("\n")


mylist = Stack()

mylist.push("munna")
mylist.push("humayun")
mylist.push("nion")
mylist.print()
print("....................")

#read last val
print(mylist.read())

#push
print(".........After push...........")
mylist.push("soyeb")
mylist.print()
print(".........After pop...........")
mylist.pop()
mylist.print()

print(".........check empty...........")
val=mylist.is_empty()
print(val)


print("...................................................")


#! now reverse a string using this 
print("now reverse a string using this ?")
string= "my name is munna"

revrce=Stack()
for i in string:
    revrce.push(i)
revrce.print()

balti=""
for i in string:
    balti=balti+revrce.pop()

print(balti)

