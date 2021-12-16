
class InstanceCounter(object):
    count=0
    def __init__(self,val):
        self.val = val
        InstanceCounter.count+=1

    def set_val(self,newval):
        self.val = newval
    
    
    def get_val(self):
        return self.val
    
    # @classmethod
    # def get_count(cls):
    #     return InstanceCounter.count

    @classmethod
    def get_count(cls):     #class method argument a sai class ta e pai
        return cls.count

a=InstanceCounter(10)
b=InstanceCounter(20)
c=InstanceCounter(30)


for i in (a,b,c):
    print(i.get_val())
    print("count=",i.get_count())

print("classmethod can be called by class")
print(InstanceCounter.get_count())