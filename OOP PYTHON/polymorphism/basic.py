
#!method overriding and overloading

import abc
class GetSetParent(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self,value):
        self.value =0

    def set_val(self,value):
        self.value =value

    def get_val(self):
        return self.value

    @abc.abstractmethod
    def showdoc(self):
        return

class GetSetInt(GetSetParent):

    def set_val(self,value):
        if not isinstance(value,int):
            value=0
        else:
            super(GetSetInt,self).set_val(value)

    def showdoc(self):
        print('GetSetInt object ({0}),only axxepts integer values'.format(id(self)))


class GetSetList(GetSetParent):

    def __init__(self,value=0):
        self.valuelist=[value]

    def set_val(self,value):
        self.valuelist.append(value)

    def get_val(self):
        return self.valuelist[-1]

    def get_vals(self):
        return self.valuelist

    @abc.abstractmethod
    def showdoc(self):
        print('GetSetList object len ({0}) stors history of values set'.format(len(self.valuelist)),)







x=GetSetInt(3)
x.set_val(5)
print(x.get_val())
x.showdoc()

print(".....................................")

gsl=GetSetList(5)
gsl.set_val(10)
gsl.set_val(20)
print(gsl.get_val())
print(gsl.get_vals())
gsl.showdoc()