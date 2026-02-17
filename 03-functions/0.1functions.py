## FUNCTION

## 1. Introduction 
# named block of code that performs a specific task  
# you write it once, use it many times  
# makes code cleaner, reusable, easier to read

# Why use ? 
# Avoid repeating the same code
# Easier to test & fix bugs  
# Makes big programs manageable

## 2. Defining Functions 
# Basic syntax:
def function_name():
    print("something")


# First example- no parameters and return
def say_hello():
    print("hello everyone!")
    print("welcome to python")

# call/run the function
say_hello()
say_hello()   # can call many times


# Key points 
# `def` keyword
# function name (snake_case recommended)
# parentheses `()`
# colon `:`
# indentation (4 spaces)

## 3. Calling Functions
def greet():
    print("good morning!")
greet()          # this is calling / invoking
print("--")
greet()
# function does nothing until you call it with `function_name()`

## 4. Function Parameters 
# Parameters = inputs to the function
def greet_person(name):           # name is parameter
    print("hello", name)
    print("how are you?")
greet_person("alex")              # "alex" is argument
greet_person("sara")


# Multiple parameters:
def add_numbers(a, b):
    result = a + b
    print("sum is", result)
add_numbers(10, 7)
add_numbers(3, 8)


# Order matters:
def introduce(name, age):
    print("my name is", name, "and i am", age, "years old")
introduce("riya", 22)      


## 5. Default Parameters 
# You can give default values – optional arguments
def greet(name="guest"):
    print("welcome", name)
greet("mohan")    
greet()            

# Multiple defaults:
def order_food(item="pizza", size="medium"):
    print("you ordered", size, item)

order_food()                
order_food("burger")         
order_food("soda", "large")  
order_food(size="small")      

## 6. Variable-Length Arguments 
# When you don’t know how many arguments will come
# Two ways:

# 1.(non-keyword arguments – tuple)
def add_many(*numbers):
    total = 0
    for num in numbers:
        total += num
    print("total =", total)

add_many(5, 3)             
add_many(1, 2, 3, 4, 5)   
add_many()                 

# 2.(keyword arguments – dictionary)
def show_info(**info):
    for key, value in info.items():
        print(key, "→", value)
show_info(name="neha", age=24, city="delhi")

# combo:
def person_details(name, *hobbies, **extra):
    print("name:", name)
    print("hobbies:", hobbies)
    print("extra info:", extra)

person_details("karan", "cricket", "music", "gaming", city="mumbai", job="student")

## 7. Return Statement 
# Functions can give back a result using `return`
def square(num):
    return num * num
result = square(6)
print(result)       
print(square(9))       


# Multiple returns (but only one runs):
def check_number(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

print(check_number(10))  
print(check_number(-5))  

# No return = returns `None` by default
def say_hi():
    print("hi")

x = say_hi()    
print(x)        

# example
def calculate_bill(items, discount=0):
    total = sum(items)
    final = total-(total * discount / 100)
    return round(final, 2)
prices = [450, 120, 890, 299]
print(calculate_bill(prices))           
print(calculate_bill(prices, 10))       


