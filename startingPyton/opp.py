from re import X
from unicodedata import name


def sum(n):
    if n==1:
        return 0
    return n + sum(n-1)

print(sum(5))

# Class ====  #

class MyClass:
    print('hello from class')
    a = 'var in class'
    def func(self):
        print('class func')

my_class = MyClass()
#print(my_class.a)
#print(my_class.func())

class House:
    rooms = 5
    bath = 2
    def evalu(self):
        print(self.rooms)
        pass


class Ricipe():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y 
    def my_func(self):
        print('cordone: x => '+ self.x + '\n         y => '+self.y)


my_class = Ricipe('233','786')

my_class.my_func()

# ==========================================
class Payment:
    def __init__(self, name,payment,amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount
    def pay(self):
        self.payment = 'yes'

    def status(self):
        if self.payment == 'yes':
            return self.name + " is paid: " + str(self.amount)
        else:
            return self.name + " is not paid yet"

salah = Payment('Salah',"no",1000)
ahmad = Payment('ahmad',"no",2000)

print( salah.status())
print( ahmad.status())

salah.pay()
print("after payment \n", salah.status())
print( ahmad.status())

