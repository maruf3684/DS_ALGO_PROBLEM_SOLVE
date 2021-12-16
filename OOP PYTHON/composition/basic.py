
class Salary(object):
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus

    def annulSalary(self):
        return self.pay*12 + self.bonus

class Employee():
    def __init__(self,name,age,pay,bonus):
        self.name = name
        self.age = age
        self.obj_salary=Salary(pay,bonus)

    def totalSalary(self):
        print(self.obj_salary.annulSalary())

max=Employee("max",25,10000,2000)
max.totalSalary()