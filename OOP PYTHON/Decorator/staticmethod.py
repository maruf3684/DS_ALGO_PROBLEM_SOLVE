
class InstanceCounter(object):
    count=0
    def __init__(self,val):
        self.val = self.filter(val)
        InstanceCounter.count+=1

    def set_val(self,newval):
        self.val = newval
    
    
    def get_val(self):
        return self.val
    
    @staticmethod                   #static method (self,cls) kono argument neba na 
    def filter(value):
        if value%2==0:
            return value
        else:
            return 0

    @staticmethod                   #static method class diye call kora jai
    def pprinting():
        print("i am static method")


    @classmethod
    def get_count(cls):     #class method argument a sai class ta e pai
        return cls.count

a=InstanceCounter(5)
b=InstanceCounter(20)
c=InstanceCounter(30)


for i in (a,b,c):
    print(i.get_val())
    print("count=",i.get_count())

InstanceCounter.pprinting()
