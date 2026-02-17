"""
magic methods in python (also called dunder methods— double underscore methods) are special methods with names like __init__, __str__, __add__ etc. 
in simple words: they are the "secret hooks" python calls automatically in certain situations.
"""

### 1. __init__: (the one you already know)
# called automatically when you create an object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("mehwish", 25)   # __init__ runs here

### 2. __str__: controls what `print(object)` shows
# without it- prints ugly memory address  
# with it- nice readable string
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def __str__(self):
        return f"a beautiful {self.color} {self.brand}"

my_car = Car("swift", "red")
print(my_car)           # a beautiful red swift


### 3. __repr__: "official" string (for developers)
# used in repl, debugging, when you just type object name
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __repr__(self):
        return f"Book(title='{self.title}', pages={self.pages})"

b = Book("python crash course", 550)
print(b)          # Book(title='python crash course', pages=550)


### 4. __add__: makes + operator work on your objects
class Money:
    def __init__(self, amount):
        self.amount = amount
    
    def __add__(self, other):
        return Money(self.amount + other.amount)
    
    def __str__(self):
        return f"₹{self.amount}"

m1 = Money(500)
m2 = Money(300)
total = m1 + m2
print(total)          


### 5. __len__: makes len() work
class Playlist:
    def __init__(self):
        self.songs = []
    
    def add(self, song):
        self.songs.append(song)
    
    def __len__(self):
        return len(self.songs)

p = Playlist()
p.add("shape of you")
p.add("perfect")
p.add("believer")
print(len(p))         


### 6. __getitem__: makes obj[index] work like list/dict
class Team:
    def __init__(self):
        self.players = ["virat", "rohit", "rahul"]
    
    def __getitem__(self, index):
        return self.players[index]

india = Team()
print(india[0])      
print(india[1])       


### 7. __eq__: makes == compare your objects properly
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

p1 = Point(3, 4)
p2 = Point(3, 4)
print(p1 == p2)       



