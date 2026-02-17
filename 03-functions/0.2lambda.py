### Lambda Functions

# lambda function is a small, anonymous(no name) function you create in one line.  
# it's perfect for short, simple tasks — especially when you need a function just once or to pass as an argument (like to `map()`, `filter()`, `sorted()`).

### Syntax 
lambda arguments : expression
# `lambda` keyword  
# arguments (like normal function parameters)  
# colon `:`  
# one single expression (this gets returned automatically)

# noted= no `def`, no function name, no `return` keyword needed.

## examples
# 1. Add 10 to a number
add_ten = lambda x: x + 10
print(add_ten(5))  


# 2. Multiply two numbers
multiply = lambda a, b: a * b
print(multiply(4, 3))  

# 3. Check if even
is_even = lambda n: n % 2 == 0
print(is_even(10))  
print(is_even(7))    


## Common Cases
# map()– apply to every item in a list
numbers = [1, 2, 3, 4, 5, 6]
squares = list(map(lambda x: x**2, numbers))
print(squares)

# filter()– keep only items that match condition
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers)) 
print(evens)

# sorted()– custom sorting
names = ["alex", "sara", "bob", "david"]
sorted_by_length = sorted(names, key=lambda name: len(name))
print(sorted_by_length)   

# With sorted() on list of tuples(sort by second value)
points = [(2, 5), (1, 8), (7, 3), (4, 4)]
sorted_points = sorted(points, key=lambda p: p[1])
print(sorted_points)  

## Comparison
# normal
def add_ten(x):
    return x + 10

# Lambda (same thing, shorter):
add_ten = lambda x: x + 10

## note 
# Complex logic (more than 1-2 lines)- use normal `def`  
# Need docstring, multiple statements, or debugging- use `def`
