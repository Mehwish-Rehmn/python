""" 
what is a generator? 
a generator is a special kind of function that doesn't return everything at once, instead, it gives you one value at a time when you ask for it, and remembers where it stopped.
-it's like a vending machine:
you press button- gets one snack
press again- next snack
no need to take out the whole machine at once
"""
# nrmal function
def get_numbers():
    return [1, 2, 3, 4, 5]   # gives whole list immediately
# generato function
def get_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

#example

def count_to_three():
    print("starting...")
    yield 1
    print("gave 1")
    yield 2
    print("gave 2")
    yield 3
    print("gave 3")

g = count_to_three()   # nothing prints yet

print(next(g))         # starting...   1
print(next(g))         # gave 1   2
print(next(g))         # gave 2   3

# common way
def even_numbers_up_to(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

for num in even_numbers_up_to(10):
    print(num)



# generator with list comprehension style
squares = (x**2 for x in range(10))   # notice ( ) not [ ]

print(next(squares))   # 0
print(next(squares))   # 1
print(next(squares))   # 4