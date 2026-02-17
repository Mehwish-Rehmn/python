"""
decorators in python are like gift wrappers for functions.
you take a normal function, wrap it with some extra magic (the decorator), and when you call the wrapped function, the magic runs automatically — before, after, or around the original function.
it's super useful for:

logging when function runs
checking permissions
timing how long function takes
caching results
turning functions into something else
"""
#normal function
def say_hello():
    print("hello")

# basic
def my_decorator(func):
    def wrapper():
        print("starting...")
        func()           # call original function
        print("finished!")
    return wrapper

@my_decorator          # this is the magic line
def say_hello():
    print("hello")

say_hello()


#decorator that takes arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)             # run function 3 times
def greet(name):
    print(f"hi {name}!")

greet("alex")


#decorator with login check
def login_required(func):
    def wrapper(user):
        if user.get("logged_in", False):
            return func(user)
        else:
            print("please login first!")
    return wrapper

@login_required
def see_profile(user):
    print(f"welcome {user['name']}")

# test
user1 = {"name": "alex", "logged_in": True}
user2 = {"name": "guest", "logged_in": False}

see_profile(user1)   
see_profile(user2)   