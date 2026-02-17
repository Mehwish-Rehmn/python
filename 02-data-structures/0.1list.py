## LIST

# list is like a shopping bag or to-do list
# Ordered: things stay in the order you put them
# changeable (mutable): you can add, remove, change items later
# can store different types together: numbers, text, booleans…
# quick example: `friends= ["Aisha", "Rahul", 15, True]`

## 2. Creating Lists (45 sec)
# Empty list: `scores = []`
# with values: `colors = ["red", "blue", "green"]`
# from other things:
  # list("hello")`:  `['h','e','l','l','o']`
  # list(range(5))`:  `[0,1,2,3,4]`
# using `split()`: `"apple banana mango".split()` → list of words

## 3. Accessing List Elements 
# Index starts at 0
# `colors[0]`: first item
# `colors[-1]`: last item
# `colors[-2]`: second last
# indexError if number too big: common beginner mistake

## 4. Modifying List Elements 
# Lists are changeable!
# `colors[1] = "yellow"`
# `colors[0] = 100` (can change type too)
# Very different from strings (strings cannot be changed like this)

## 5. List Methods # important
# `.append(x)`: add one item at end
# `.extend([a,b])` or `+= [a,b]`: add many items
# `.insert(position, value)`
# `.pop()`: remove & return last item
# `.pop(2)`: remove item at index 2
# `.remove("apple")`: remove first "apple"
# `.clear()`: empty the list
# `.index("blue")`: find position
# `.count(7)`: how many times 7 appears
# `.sort()` / `.reverse()`

## 6. Slicing Lists 
# `list[start:end]`: from start to end-1
# `list[1:4]`: items 1,2,3
# `list[:3]: first 3 items
# `list[2:]: from index 2 to end
# `list[:]`: full copy
# `list[::2]`: every second item
# `list[::-1]`: reversed list

## 7. Iterating Over Lists 
fruits= ["apple", "banana", "papaya", "kiwi", "grapes"]
# common way
for fruit in fruits:
      print(fruit)

# With index:
for i in range(len(fruits)):
      print(i, fruits[i])

# With both index & value:
for idx, item in enumerate(fruits):
      print(idx, item)


## 9. Nested Lists 
# List inside list= like table/matrix

matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
  ]

## simple example

# empty list 
friends = []
# list with same type of items
marks = [85, 92, 78, 65]
# list with different types of items 
random_stuff = [23, "hoph", 3.14, True, "Delhi"]
# shopping list 
shopping = ["milk", "bread", "eggs", "butter"]