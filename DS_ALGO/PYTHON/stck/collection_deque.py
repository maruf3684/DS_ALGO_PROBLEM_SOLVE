
from collections import deque
print(type(deque))
#deque neza e akta class jaita type class er object

stack=deque()
print(type(stack))
#stack nam a deque class er object banlam amra

print(dir(stack))
#stack object diye amra deque class er uporokto class gular access pabo


#lets append to stack 
stack.append("munna")
stack.append("nion")
stack.append("humaun")

print(stack)

#lets pop from stack
stack.pop()
print(stack)

#loop through stack 
for i in stack:
    print(i)





