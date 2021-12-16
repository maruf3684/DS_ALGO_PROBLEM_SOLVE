
class A(object):
    def doThis(self):
        print("Do this in A")

class B(A):
    pass

class C(object):
    def doThis(self):
        print("Do this in C")



#!work will like depth first search
class D(B,C):
    pass


#D er instance bania do this call korle kar ta ashbe


d_instance=D()
d_instance.doThis() #and: do this in A

#lookup order 
print (D.mro())

#!work will like depth first search