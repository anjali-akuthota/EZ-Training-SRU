#Constructor Overloading
class Anjali():
    def __init__(temp1):
        print("C is best")
    def __init__(temp, temp1=''):
        print("Java is best")
    def __init__(temp, temp1='', temp2=''):
        print("Python is best")


obj = Anjali()
obj1 = Anjali(100)
obj2 = Anjali(100, 200)