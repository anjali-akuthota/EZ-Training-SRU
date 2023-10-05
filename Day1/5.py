#Polymorphism
class Icecream:
    def cravings(x):
        print("Icecreams are best")

class Chocolate(Icecream):
    def cravings(x):
        print("I hate Chocolate")

class Butterscotch(Icecream):
    def cravings(x):
        print("I love Butterscotch")


ice = [Icecream(), Chocolate(), Butterscotch()]
for obj in ice:
    obj.cravings()
