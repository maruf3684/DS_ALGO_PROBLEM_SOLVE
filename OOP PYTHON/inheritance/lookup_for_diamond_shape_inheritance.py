
class A(object):
    def doThis(self):
        print("Do this in A")

class B(A):
    pass

class C(A):
    def doThis(self):
        print("Do this in C")

class D(B,C):
    pass


#D er instance bania do this call korle kar ta ashbe


d_instance=D()
d_instance.doThis() #and: do this in A

#lookup order 
print (D.mro())

#![<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
#!lass lookup er array theke 1st occured duplicate class ta bad jabe