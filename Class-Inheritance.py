# Inheritance is a way of creating a new class for using details of an existing class without modifying it.

class Animal:
    def eat(self):
        print("I can eat")
    def run(self):
        print("I can run")

class dog(Animal):
    def bark(self):
        print("i can bark")


class cat(Animal):
    def meow(self):
        print(" I can Communicate via meow")


dog1 = dog()
print("Dog details")
dog1.eat()
dog1.run()
dog1.bark()

Cat1 = cat()
print("Cat details")
Cat1.eat()
Cat1.run()
Cat1.meow()
