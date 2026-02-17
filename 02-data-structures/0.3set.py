## SETS
# collection of uniue items
# unordered: no fixed position/order
# mutable: you can add/remove items (but you cannot change existing ones)
# items must be immutable(numbers, strings, tuples- not lists or dicts)
# written with curly braces {}
# removing duplicates, membership check (`in`), math operations (union, intersection)

## 2. Creating Sets
# Way 1: curly braces
fruits = {"apple", "banana", "mango"}
# way 2: from list (removes duplicates automatically)
numbers = set([1, 2, 2, 3, 1, 4])  
# Empty set (important!)
empty = set()    

## 3. accessing Set Elements
# No index! You can only check if something is inside
print("apple" in fruits)    # True
print("grapes" in fruits)   # False

# you CAN loop
for fruit in fruits:
    print(fruit)            # order random every time

## 4. set Operations 
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# Union (all items)
print(a | b)         
print(a.union(b))
# Intersection (common)
print(a & b)       
print(a.intersection(b))
# Difference (a has but b doesn't)
print(a - b)      
print(a.difference(b))
# Symmetric difference (unique to each)
print(a ^ b)    

## 5. Mutable Nature of Sets
colors = {"red", "blue"}
colors.add("green")   # OK
colors.remove("blue")  # OK
# colors[0] = "pink"  # Error! No indexing
# colors.add([1,2])  # Error! List not allowed
colors.add((1,2))  # OK- tuple is immutable

## 6. Set Methods 
s = {10, 20, 30}
s.add(40)   # add one
s.update([50, 60])  # add many 
s.remove(20)  # error if not found
s.discard(99)   # no error if not found
s.pop()  # remove & return random item
s.clear()  # empty set
len(s)  # count items

## 7. No Packing/Unpacking like tuples (but can unpack in loops)
x, y, z = {1, 2, 3}    

## 8. Nested Sets?: Not directly (sets can't contain sets)
# But you can use "frozenset" (immutable set)
fs = frozenset([1, 2, 3])
nested = {fs, "hello"}   

## 9. example
# remove duplicates from list
names = ["rahul", "jacob", "rahul", "aisha"]
unique = set(names)      

## 10. Example
# find common friends
my_friends = {"ali", "sara", "rahul"}
her_friends = {"sara", "mehwish", "rahul"}
common = my_friends & her_friends   

# Common errors
# s[0]               → TypeError: 'set' object is not subscriptable
# s.add([1,2])       → TypeError: unhashable type: 'list'
# s.remove(999)      → KeyError if not present (use discard instead)
# {}                 → this is dict, not set!