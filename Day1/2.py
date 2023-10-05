#Hierarchical and Multi-level Inheritance
class Anjali:
    def method1(temp):
        print("Hi")
    def method2(temp):
        print("all")
class Anju1(Anjali):
    def method3(temp):
        print("Welcome")
class Anju2(Anjali):
    def method4(temp):
        print("to my")
class Anju3(Anju1,Anju2):
    def method5(temp):
        print("World")
obj1=Anju1()
obj2=Anju2()
obj3=Anju3()
obj1.method1()
obj2.method1()
obj3.method1()