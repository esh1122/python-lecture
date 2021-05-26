class Cat :

    def __init__(self, name, age, color = '흰색') :
        self.name = name
        self.color = color
        self.age = age

    def __str__(self) :
        return "Cat(name=" + self.name + ',color=' + self.color + ',age=' + str(self.age) +')' 

    def set_age(self, age) :
        self.set_age(self)

    def get_age(self) :
        return self.get_age


nabi = Cat('나비', 4)
nero = Cat('나비', 5, '검정색')

print(nabi)
print(nero)