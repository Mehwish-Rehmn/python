'''
Polymorphism
is one of the most beautiful and practical ideas- it literally means “many forms”.
It lets you use one interface(same method name) for different types of objects- and each object does its own version of the work.

 Why powerful?

You can write code that works with many types without knowing exactly what they are.
Example: for shape in shapes: shape.area() works even if you add triangle, square later.
Code becomes flexible, reusable, and easy to extend.
'''
### How it works in Python 

# Parent class with a method
class Animal:
    def make_sound(self):
        print("some generic animal sound")

# Child classes override the same method
class Dog(Animal):
    def make_sound(self):
        print("woof woof!")

class Cat(Animal):
    def make_sound(self):
        print("meow meow!")

class Cow(Animal):
    def make_sound(self):
        print("moo moo!")


# Now see polymorphism in action
animals = [Dog(), Cat(), Cow(), Animal()]

for animal in animals:
    animal.make_sound()
    

'''
Note:
We called the same method name `make_sound()` on different objects.
Each object did its own version of the action.
This is polymorphism.

 Two main types of polymorphism you’ll see
# 1. Method overriding- Child class changes(overrides) the parent’s method with the same name.
# 2. Method overloading-  In Python, we usually handle it by: default parameters; args/kwargs; or different types of input
'''
# Example (Python style “overloading”):
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5))        
print(calc.add(5, 10))   
print(calc.add(5, 10, 15)) 

# Another real-world example 
class Shape:
    def area(self):
        return 0  # base version

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2


shapes = [Rectangle(4, 5), Circle(3), Shape()]

for shape in shapes:
    print("area =", shape.area())
    

# Same method `area()`- different calculations for different shapes.



'''
Method overriding:
Is one of the most important and powerful mechanisms in object-oriented programming (especially in Python).
It is the situation when a child class redefines (overrides) a method that already exists in the parent class— with the same name, same number of parameters, but usually with different behavior.
This is the heart of polymorphism(same method name- different actual action).

What exactly gets overridden?
Only the method body is replaced.  
The method signature (name + parameters) must stay the same.
'''
class Parent:
    def greet(self, name):
        print(f"Hello {name} from parent")

class Child(Parent):
    def greet(self, name):               # same name, same parameters
        print(f"Hi {name}! I'm the child version 😄")


#### 2. How Python decides which version to run (method resolution)
# Python uses the **MRO** (Method Resolution Order) — but in simple inheritance it's very straightforward:
"""
First look inside the object's own class
If not found look in parent
If not found- grandparent, etc.
"""
c = Child()
c.greet("ALEX")     
                        

p = Parent()
p.greet("ALEX")    
                    
#### 3. Most common real patterns
## Pattern A – completely different behavior**
class Shape:
    def draw(self):
        print("drawing generic shape")

class Circle(Shape):
    def draw(self):
        print("drawing a circle ⭕")

class Square(Shape):
    def draw(self):
        print("drawing a square ⬜")


## Pattern B – extend parent's behavior (use super())**
class Employee:
    def work(self):
        print("doing normal office work")

class Developer(Employee):
    def work(self):
        super().work()                    # call parent's version first
        print("   + writing python code")
        print("   + debugging at 2 AM")


## attern C– change parameters slightly (still same signature)

class Printer:
    def print_page(self, content):
        print("printing:", content)

class ColorPrinter(Printer):
    def print_page(self, content):
        print("printing in color:", content.upper())


''' 4. Important rules
1. Method name and number of parameters must match exactly  
def greet(self, name) in parent  
cannot be def greet(self) or def greet(self, name, age) in child (that would be new method, not override)
2. Return type can be different (Python doesn't care)
3. You can make child method **stricter** or **more specific**
4. `@override` decorator does **not** exist in Python (unlike Java)  
   → but many people use it anyway as documentation:
'''
