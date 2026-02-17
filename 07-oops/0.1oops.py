""" 
OOPS
Object Oriented Programming System
It's a way to write code by thinking in terms of real-world things (objects) instead of just functions and data separately.

Think of it like this:
Without OOP: you have loose variables + loose functions
With OOP: you bundle data + behavior together into “things” (objects)

Example from real life:
A car has-
Data: color, speed, fuel level (attributes)
Behavior: drive(), stop(), honk() (methods)

In OOP, you create a class car that describes what every car can do, then make many car objects.

The 4 main pillars of OOP
Class: blueprint/template
Object: real thing made from the blueprint
Inheritance: child class gets features from parent
Encapsulation: hide internal details, show only what's needed
Polymorphism: same method name does different things

"""

## example (easy)
# 1. Create a class (blueprint)
class Dog:
    # special method that runs when we make a new dog
    def __init__(self, name, age, color):
        self.name = name     
        self.age = age       
        self.color = color    

    # actions (methods)
    def bark(self):
        print(f"{self.name} says: Woof woof!")

    def run(self):
        print(f"{self.name} is running happily!")

    def birthday(self):
        self.age = self.age + 1
        print(f"Happy birthday! {self.name} is now {self.age} years old")


# 2. Make real dogs (objects) from the blueprint
dog1 = Dog("max", 3, "brown")
dog2 = Dog("lucky", 1, "white")

# 3. Use them
dog1.bark()         
dog2.bark()         

dog1.run()         

dog1.birthday()     
print(dog1.age)    


## Now let’s add the other 3 ideas

# 4. Inheritance (child class gets parent features)
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sleep(self):
        print(f"{self.name} is sleeping")

# Child class (inherits from Animal)
class Cat(Animal):
    def meow(self):
        print(f"{self.name} says: Meow meow!")

# Create cat
my_cat = Cat("whiskers")
my_cat.sleep()      # whiskers is sleeping (got from parent)
my_cat.meow()       # whiskers says: Meow meow!

# 5. Encapsulation (hide data + control access)
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private (hidden with __)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Added {amount}. New balance: {self.__balance}")
        else:
            print("Amount must be positive")

    def get_balance(self):
        return self.__balance   # only way to see balance

# Use it
account = BankAccount("alex", 5000)
account.deposit(2000)         

# print(account.__balance)   # ERROR – hidden!
print(account.get_balance())  

"""
practice task 
1. Create a class `Car`
2. Give it: brand, color, speed = 0
3. Make methods: accelerate()- speed + 20, brake()- speed - 10 (don’t go below 0)
4. Create 2 cars, play with them
"""

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0
    
    def accelerate(self):
        self.speed += 20
        print(f"{self.brand} speed is now {self.speed} km/h")
    
    def brake(self):
        self.speed = max(0, self.speed - 10)
        print(f"{self.brand} slowed to {self.speed} km/h")

car1 = Car("swift", "red")
car1.accelerate()
car1.accelerate()
car1.brake()
