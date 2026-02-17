## DICTIONARIES
# Dictionaries (or "dicts") are unordered, changeable collections of key-value pairs. They use curly braces {} and colons : to separate keys and values.
# Why use them? Fast lookups by key, no duplicates in keys.
# Example: Store student info where "name" is key, "Mehwish" is value.
# Introduced in Python 3.7+, they keep insertion order.

## 1. Creating Dictionaries
# Use {} with key-value pairs, or dict() function.

# Empty dict
empty_dict = {}

# With data
person = {"name": "Jacob", "age": 25, "city": "Delhi"}

# Using dict()
colors = dict(red=1, blue=2, green=3)

print(person)  

## 2. Accessing Dictionary Elements
# Use square brackets [] with the key, or .get() to avoid errors if key missing.

person = {"name": "Jacob", "age": 25}

print(person["name"])  
print(person.get("age"))  
print(person.get("job", "Not found"))  
# noted: If key doesn't exist: [] gives KeyError, .get() returns None or default.

## 3. Modifying Dictionary Elements
# Dictionaries are mutable — add, update, or remove items easily.

person = {"name": "Jacob"}

# Add new
person["age"] = 25

# Update existing
person["age"] = 26

# Remove
del person["age"]  

print(person)  

## 4. Dictionary Methods
# Common ones:

# keys(): Get all keys.
# values(): Get all values.
# items(): Get key-value pairs.
# update(): Merge another dict.
# clear(): Empty the dict.
# popitem(): Remove last item.

person = {"name": "Jacob", "age": 25}
print(person.keys())    
print(person.values())  
person.update({"city": "Delhi"})
print(person)  

## 5. Iterating Over Dictionaries
# Use loops to go through keys, values, or both.

person = {"name": "Jacob", "age": 25, "city": "Delhi"}
# Over keys (default)
for key in person:
    print(key)  
# Over values
for value in person.values():
    print(value)  
# Over both
for key, value in person.items():
    print(key, ":", value) 

## 6. Nested Dictionaries
# Dict inside a dict — like a tree of data.
 
students = {
    "student1": {"name": "Jacob", "age": 25},
    "student2": {"name": "Alex", "age": 22}
}

print(students["student1"]["name"])  

## 7. Dictionary Comprehensions
# Short way to create dicts from loops (like list comprehensions).

# Square numbers
squares = {x: x**2 for x in range(1, 4)}
print(squares)  # {1: 1, 2: 4, 3: 9}

# From list
names = ["jacob", "alex"]
upper_dict = {name: name.upper() for name in names}
print(upper_dict)  

## 8. examples 

phone_book = {"Jacob": "123-456", "Alex": "789-012"}
name = input("Name: ")
number = input("Number: ")
phone_book[name] = number

# Lookup
search = input("Search name: ")
print(phone_book.get(search, "Not found"))

##Common Errors:

# KeyError: Accessing missing key: fix with .get().
# TypeError: Using mutable keys like lists: keys must be immutable.
# Overwriting: Duplicate keys replace old value (last one wins).
# Forgetting quotes: Keys like strings need "k ey".

