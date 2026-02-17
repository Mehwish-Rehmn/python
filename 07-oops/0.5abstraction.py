"""
ABSTRACTION
in oops is one of the four main pillars (along with encapsulation, inheritance, polymorphism).
in the simplest words:
abstraction means hiding the complicated internal details and showing only the necessary and useful parts to the user.
it's like using a tv remote:
you press power, volume, channel buttons
you don't need to know how circuits, signals, electricity, or screen pixels work inside
the remote hides complexity and gives you a simple interface

in programming, abstraction does the same:
you give the user a clean, simple way to use your class
you hide all the hard, boring, or dangerous internal logic

two main ways abstraction is achieved in python
abstract classes (using abc module)- most common and strict way
regular classes with encapsulation (hide details using private/protected + public methods)
"""

#### 1. abstract classes 
from abc import ABC, abstractmethod

#  abstract class (cannot create object from it)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # no body– child must implement

    @abstractmethod
    def perimeter(self):
        pass

# child classes must provide real implementation
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius


# now use them
shapes = [Rectangle(4, 5), Circle(3)]

for shape in shapes:
    print("area:", shape.area())
    print("perimeter:", shape.perimeter())

'''important points:
you cannot create object from abstract class- Shape() will give error
every child must implement all abstract methods
if child forgets- error when creating object'''

#### 2. abstraction using regular classes + encapsulation
## even without abc module, you can achieve abstraction by:
#making internal details private
#giving only simple public methods

class CoffeeMachine:
    def __init__(self):
        self.__water = 1000  # ml – hidden
        self.__coffee_powder = 500  # grams – hidden
        self.__milk = 800  # ml – hidden

    # simple public interface – user only needs these
    def make_espresso(self):
        if self.__water >= 50 and self.__coffee_powder >= 7:
            self.__water -= 50
            self.__coffee_powder -= 7
            print("espresso ready! ☕")
        else:
            print("not enough ingredients")

    def make_latte(self):
        if self.__water >= 50 and self.__coffee_powder >= 7 and self.__milk >= 200:
            self.__water -= 50
            self.__coffee_powder -= 7
            self.__milk -= 200
            print("latte ready! 🥛☕")
        else:
            print("not enough ingredients")

    def refill(self):
        self.__water = 1000
        self.__coffee_powder = 500
        self.__milk = 800
        print("machine refilled")


machine = CoffeeMachine()
machine.make_espresso()     # espresso ready!
machine.make_latte()        # latte ready!
machine.refill()