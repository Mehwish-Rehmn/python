"""
Inheritance in OOPS
Is one of the most powerful and useful ideas in object-oriented programming.

real-life analogy:
Imagine you have a parent dog and a puppy.
The puppy automatically gets many things from the parent:
four legs
tail
ability to bark
fur color possibilities

But the puppy can also have extra things or do things differently:
maybe it has a shorter tail
maybe it barks louder or differently

In OOPS:
- The parent= base class/super class/parent class
- The puppy = child class/derived class/sub class

The child inherits (gets for free) almost everything from the parent, and then it can:
- add new things
- change (override) some behaviors
- use everything as-is
"""

## Very simple code exampl
# Parent class (base class)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating food")
    
    def sleep(self):
        print(f"{self.name} is sleeping")


# Child class (inherits from Animal)
class Dog(Animal):           #  this (Animal) means Dog inherits from Animal
    def bark(self):          # new method- parent didn't have this
        print(f"{self.name} says: Woof woof!")
    
    def eat(self):           # overriding (changing) parent's eat method
        print(f"{self.name} is eating dog food happily")


# Create objects
a = Animal("some animal")
d = Dog("max")

a.eat()       
d.eat()       
d.sleep()     
d.bark()      

#### Key points to remember (very easy list)

'''
1. Syntax to inherit 
class Child(Parent):     # your new code here

2. Child gets everything from parent
attributes (like name, age)
methods (like eat, sleep)  
(unless you change them) 

3. Three common things you do in child class
add new methods / attributes  
override (change) parent methods  
use parent's methods as-is

4. super()- call parent's method 
Very useful when you want parent's behavior + extra

'''

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)          # call parent's __init__
        self.breed = breed              # add extra attribute


"""
class ElectricCar(Car):  
Car has wheels, engine- ElectricCar adds battery, charging

class Manager(Employee): 
Employee has name, salary- Manager adds bonus, team_size

class SavingAccount(BankAccount):  
BankAccount has deposit/withdraw- SavingAccount adds interest calculation
"""

