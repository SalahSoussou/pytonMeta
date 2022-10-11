from unicodedata import name


class Parant:
    def __init__(self, name,last) -> None:
        self.name = name
        self.last = last


class Childe_1(Parant):
    def __init__(self, name, last, age) -> None:
        super().__init__(name, last)
        self.age = age


class Childe_2(Parant):
    def home_work(self, time):
        return 'I need ' +str(time) + " min to do my home mork"

salah = Parant('salah',"S")


soussou = Childe_1('Sou',"U",12)
ous = Childe_2('Ous',"S")

print(ous.home_work(60))

print(soussou.age)
print(ous.name)