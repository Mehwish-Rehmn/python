"""
operator overloading in python is a very cool feature of oops.
it means:
you can change/define how operators like +, -, *, ==, >, < etc. work when they are used with your own objects (custom classes).
normally + works only on numbers or strings, but with operator overloading you can make + do whatever you want when used between two of your objects.
simple definition 
"operator overloading = teaching python new tricks for symbols like + - * == when they meet your custom class objects"
why it is useful?
without it:
you have to write ugly code like v1.add(v2) instead of clean v1 + v2
with it:
your objects behave like built-in types (int, list, str) → code looks natural and beautiful
"""
### very simple real examples

#### example 1 – add two money objects

class Money:
    def __init__(self, rupees):
        self.rupees = rupees
    
    def __add__(self, other):
        # other can be another Money or a number
        if isinstance(other, Money):
            return Money(self.rupees + other.rupees)
        elif isinstance(other, (int, float)):
            return Money(self.rupees + other)
        else:
            raise TypeError("can only add money or number")
    
    def __str__(self):
        return f"₹{self.rupees}"

m1 = Money(500)
m2 = Money(300)

print(m1 + m2)      # ₹800
print(m1 + 200)     # ₹700


#### example 2 – compare two students by marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.marks == other.marks
        return False
    
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.marks < other.marks
        return False
    
    def __str__(self):
        return f"{self.name} ({self.marks} marks)"

s1 = Student("alex", 85)
s2 = Student("sara", 92)
s3 = Student("riya", 85)

print(s1 == s3)     # True (same marks)
print(s1 < s2)      # True (85 < 92)
print(sorted([s1, s2, s3]))   # sorts by marks

#### example 3 – multiply vectors (very common use)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __mul__(self, scalar):
        # multiply by number (scalar)
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

v = Vector(3, 4)
print(v * 2)        # (6, 8)


"""important rules / tips

1. the left object calls the method
a + b: calls a.__add__(b)
so usually put logic in left operand's class
2. if you define __add__, you should also define __radd__ (for right-side cases)
example: 5 + money_object needs __radd__
3. always check type with isinstance()
because + can be called with different types
4. return a new object usually (don't change self)
for comparison operators (==, <, >) → return True/False"""