class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        return "I move in some way"


class Dog(Animal):
    def move(self):
        print("I move by walking")


class Fish(Animal):
    def move(self):
        print("I move by swimming")

class Kangaroo(Animal):
    def move(self):
        print("I move by hoping")


print(Dog.move)
