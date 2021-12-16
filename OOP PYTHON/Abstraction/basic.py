from abc import ABC ,abstractmethod



#!abstract class er instance toiri kora jai na
#!abstract class a abstract method akta hole o thakte hobe
#! abstract class ke kono class inherit korle sei class a abstract class er method gula thakktei hobbe must be


class Computer(ABC):
    
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("Its Running")



class programar:
    def work(self,withh):
        print("Solving bugs")
        withh.process()



dell=Laptop()
dell.process()

munna=programar()
munna.work(dell)



