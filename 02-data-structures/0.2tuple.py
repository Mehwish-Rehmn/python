## TUPLES
# tuple is an ordered, immutable (unchangeable) collection of items.
# think of it as a locked box: once you put things inside and close it, you cannot add, remove, or change anything.

## 1. Introduction to Tuples 
# ordered: items have a fixed position (index starts at 0)
# immutable: cannot modify after creation (biggest difference from lists)
# allows duplicates
# can contain mixed data types
# uses less memory than lists
# very common when data should never change (coordinates, days of week, RGB colors…)

## 2. Creating Tuples 

# Most common ways
person = ("Aisha", 24, "Delhi")              # with parentheses
scores = 85, 92, 78                          # without parentheses (tuple packing)
empty = ()                                   # empty tuple
single = (500,)                              # single item: comma is MUST!
wrong = (500)                                # this is NOT a tuple, just integer
colors = tuple(["red", "green", "blue"])     # from list
letters = tuple("hello")                     # ('h','e','l','l','o')

## 3. accessing tuple elements
#same as list: using index
person = ("Rahul", 19, "Mumbai", True)
print(person[0])     
print(person[-1])    
print(person[1:3])   

## 4. tuple Operations 

# Concatenation: t1+t2
# Repetition: t1*3
# Membership: "Delhi" in person
# Count: person.count("Delhi")
# Index: person.index(19)
# Min/Max/Sum (if numbers): min(scores), sum(scores)

## 5. immutable Nature of Tuples (1 min)
# You cannot do these:

# person[1] = 20    # Type.error
# person.append("India")  # Attribute error
# person.pop()   # Attr..error
# del person[0]    # Type error

## 6. Tuple Methods (45 sec)
# Tuples have only two methods:
t = (10, 20, 10, 30, 10)
print(t.count(10))     
print(t.index(20))     

## 7. Packing and Unpacking Tuples (1.5 min)
#Packing = putting values into tuple
# Unpacking = taking values out into variables

# Packing
point = 10, 25  # auto packing

# Unpacking
x, y = point
print(x, y)           

# Unpacking in one line
name, age, city = ("Jacob", 22, "Delhi")

# Using * to collect rest
a, b, *rest = (1, 2, 3, 4, 5)
print(a, b, rest)        
# Swap 2 variables 
x, y=y, x

## 7. Nested Tuples 
# Tuple inside tuple (like table rows)
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print(matrix[1][2])      
print(matrix[0])        

## 8. Examples
# Return multiple values from function
# Use as dictionary keys (lists cannot be keys)
# Fixed configuration values
# days of week: days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
person = ("Jacob", 22, "Delhi")
print(person[0])    
print(person[-1])    
# You can read, but you CAN'T do this:
# person[1] = 23     #error
# person.append()    #error
#trick
name, age, city = person
print(name, "is", age, "from", city)
