 #Given a sorted array A containing N integers both positive and negative.

#You need to create another array containing the squares of all the elements in A and return it in non-decreasing order.

A = [-6, -3, -1, 2, 4, 5]


Squre=[i*i for i in A]
Squre=sorted(Squre)

print(Squre)
    
