 # basic oops problem
class Car:
    name="BMW"
    color="Black"

c1 = Car()

print(c1.name)
print(c1.color)

c1 = {name:"BMW",color:"Black"}

#using self in the class

class Student:
    def student_info(self,name,age):
        print(name,age)
s1=Student()
s1.student_info("pavan",23)

#self real usage

class Car:
    name="BMW"
    color="Black"
    def speed(self):
        print(self.name,self.color)
        print("200kmph")
c1 = Car()
c1.speed()

class Car:
    name="BMW"
    color="red"
    def __init__(self):
        print("200kmph")
    def speed(self):
        print("speed executed")
c1 = Car()
c1.speed()

# 
class Car:
    wheels = 4
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
    def display(self):
        print(self.wheels)
        print(self.name)
        print(self.speed)
c1=Car("Bmw","200kmph")
c1.display()

print("\n")

c2 = Car("volvo",'100kmph')
c2.display()

# ENCAPSULATION
class Bank:
    def __init__(self):
        self.__balance = 1000
    def show_balance(self):
        print(self.__balance)
    def deposit(self,amount):
        self.__balance = self.__balance+ amount
    def withdraw(self,amount):
        self.__balance = self.__balance - amount

b1=Bank()
b1.show_balance()
b1.deposit(30000)
b1.withdraw(3000)
b1.show_balance() 

# INHERITANCE
class Employee:
    def work(self):
        print("employee is working")
class Developer(Employee):
    def code(self):
        print("developer is developing the app")
class tester(Employee):
    def test(self):
        print("tester is testing the app")
d = Developer()
d.work()
t = tester()
t.work()
t.test()
    
# POLYMORPHISM
class Employee:
    def work(self):
        print("employee is working")
class Developer(Employee):
    def execute(self):
        super().work()
    def work(self):
        print("developer is developing the app")
class tester(Employee):
    def work(self):
        print("tester is testing the app")
d = Developer()
d.execute()

#ABSTRACTION
from abc import ABC,abstractmethod

class Atm(ABC):
    @abstractmethod
    def withdraw(self):
        pass
class Sbi(Atm):
    def withdraw(self):
        print("money is withdrawn from SBI")
class Hdfc(Atm):
    def withdraw(self):
        print("money is withdrawn from HDFC")       

w=Sbi()
w.withdraw()

# excercise 1
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")
s1 = Student("pavan",21)
s1.introduce()       




 








