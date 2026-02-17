### map()

# map() is a very useful built-in function in Python.
# map() applies a function to every item in an iterable (like list, tuple, string, etc.)
# and returns a map object (you usually convert it to list or tuple).
# Basic syntax
## map(function, iterable)
# more than one iterable
## map(function, iterable1, iterable2, ...)


# examples:
list(map(lambda x: x*2, [1,2,3]))  
list(map(str.upper, ["a","b","c"]))  
list(map(int, ["1","2","3"]))

# 1. basic: square every number
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)         

# 2. add 10 to each number
add_ten = list(map(lambda x: x + 10, [5, 15, 25]))
print(add_ten)         

# 3. convert strings to integers
strings = ["10", "20", "30"]
numbers = list(map(int, strings))
print(numbers)        

# 4. uppercase all strings
words = ["apple", "banana", "cherry"]
upper = list(map(str.upper, words))
print(upper)   

# 5. two lists- add corresponding items
a = [1, 2, 3]
b = [10, 20, 30]
result = list(map(lambda x, y: x + y, a, b))
print(result)     

# 6. using normal function (not lambda)
def double(x):
    return x * 2

nums = [5, 10, 15]
doubled = list(map(double, nums))
print(doubled)       

# 7. one-liner pattern
print(list(map(str, range(1, 6))))   

