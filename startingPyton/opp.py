from re import X


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