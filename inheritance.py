# Inheritance in OOP

class Animal: # "Base class"
    def __init__(self, name):
        self.name = name
        
    def call(self):
        print(f"{self.name} Generic animal sound")

class Vertibrate(Animal):
    def call(self):
        print(f"{self.name}: Generic vertibrate sound")
    

class Mammal(Vertibrate):
    pass

class Cat(Mammal):

    def __init__(self, name, evil):
        super().__init__(name)
        self.evil = evil

    def call(self):
        print(f'{self.name} ({"evil" if self.evil else "not evil"}): Meow')

class Invertibrate(Animal):
    pass

animals = [
           Animal("animal 1"),
           Vertibrate("vert 1"),
           Invertibrate("invert 1"),
           Cat("cat 1", "not evil"),
           ]

for a in animals:
    a.call()
